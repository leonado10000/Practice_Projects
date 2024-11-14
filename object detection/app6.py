import subprocess
import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import threading
import random
import time
import pygame

class PeopleDetectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("People Detection with YOLOv5")
        self.geometry("1280x800")
        self.configure(bg="#f8f9fa")
        
        pygame.mixer.init()
        self.alarm_playing = False
        self.crowd_size_limit = 10  # Default crowd size limit

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title = tk.Label(self, text="People Detection with YOLOv5", font=("Arial", 28, "bold"), bg="#4285F4",
                         fg="white", padx=20, pady=10)
        title.pack(pady=20, fill=tk.X)

        # Team Members
        team_label = tk.Label(self, text="Team Members: Rahul Jangra, Rachana B, Sathvik N G", font=("Arial", 16),
                              bg="#f8f9fa", fg="#34A853", padx=20, pady=10)
        team_label.pack()

        # Video selection
        self.video_frame = tk.Frame(self, bg="#f8f9fa")
        self.video_frame.pack(pady=10, padx=20, fill=tk.X)

        tk.Label(self.video_frame, text="Select Video:", font=("Arial", 16), bg="#f8f9fa").grid(row=0, column=0, padx=10)
        self.video_entry = tk.Entry(self.video_frame, width=50, state='readonly', font=("Arial", 14), bd=2, relief="groove")
        self.video_entry.grid(row=0, column=1, padx=10)
        tk.Button(self.video_frame, text="Browse", command=self.browse_video, bg="#34A853", fg="white", font=("Arial", 14), width=10, relief="raised").grid(row=0, column=2, padx=10)

        # Crowd size limit input
        tk.Label(self.video_frame, text="Crowd Size Limit:", font=("Arial", 16), bg="#f8f9fa").grid(row=1, column=0, padx=10, pady=10)
        self.crowd_size_entry = tk.Entry(self.video_frame, width=10, font=("Arial", 14), bd=2, relief="groove")
        self.crowd_size_entry.grid(row=1, column=1, padx=10, pady=10)
        self.crowd_size_entry.insert(0, str(self.crowd_size_limit))  # Default value

        # People Count Display
        self.people_count_label = tk.Label(self, text="People Count: 0", font=("Arial", 18), bg="#f8f9fa", fg="#333333", pady=10)
        self.people_count_label.pack()

        # Thumbnail Display
        self.thumbnail_canvas = tk.Canvas(self, bg="white", width=640, height=360, highlightthickness=1, highlightbackground="#cccccc", relief="raised")
        self.thumbnail_canvas.pack(pady=10)

        # Control Buttons
        self.button_frame = tk.Frame(self, bg="#f8f9fa")
        self.button_frame.pack(pady=20)

        self.start_buttonY = tk.Button(self.button_frame, text="YoloV5", font=("Helvetica", 16), bg="#34A853", fg="#ffffff", command=self.yolov5_detection)
        self.start_buttonY.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.start_buttonZ = tk.Button(self.button_frame, text="Fast Rnn", font=("Helvetica", 16), bg="#34A853", fg="#ffffff", command=self.frnn_detection)
        self.start_buttonZ.pack(padx=10, pady=10)

        self.quit_button = tk.Button(self.button_frame, text="Quit", font=("Arial", 16), command=self.quit, width=15, bg="#EA4335", fg="white", relief="raised")
        self.quit_button.pack(side=tk.RIGHT, padx=20)

        # Footer Frame
        self.footer_frame = tk.Frame(self, bg="#f8f9fa")
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        footer = tk.Label(self.footer_frame, text="Made with ❤️ for People Detection", font=("Arial", 12, "italic"), bg="#f8f9fa", fg="#333333")
        footer.pack(pady=10)

        # Adding a border to the window
        self.configure(borderwidth=5, relief="ridge")

    def browse_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
        if video_path:
            self.video_entry.config(state='normal')
            self.video_entry.delete(0, tk.END)
            self.video_entry.insert(0, video_path)
            self.video_entry.config(state='readonly')
            self.show_thumbnail(video_path)

    def show_thumbnail(self, video_path):
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        n = 0
        while n<100:
            n += 1
            ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 360))
            frame_image = Image.fromarray(frame)
            frame_image_tk = ImageTk.PhotoImage(frame_image)
            self.thumbnail_canvas.create_image(0, 0, anchor="nw", image=frame_image_tk)
            self.thumbnail_canvas.image = frame_image_tk
        cap.release()

    # Dummy start detection for testing
    def start_detection(self):
        video_path = self.video_entry.get()
        if video_path:
            self.detection_thread = threading.Thread(target=self.run_detection_test, args=(video_path,))
            self.detection_thread.start()

    def run_detection_test(self):
        people_count = random.randint(1, 15)
        self.update_people_count(14)
        time.sleep(0.1)

    def update_people_count(self, count):
        try:
            self.crowd_size_limit = int(self.crowd_size_entry.get())
        except ValueError:
            self.crowd_size_limit = 10  # Default value if input is invalid
        color = "#ff0000" if count > self.crowd_size_limit else "#34A853"  # Red if > limit, Green if <= limit
        something = "Crowded" if count > self.crowd_size_limit else "Not Crowded"
        self.people_count_label.config(text=f"People Count: {count} detected, {something}", fg=color)
        if count > self.crowd_size_limit:
            if not self.alarm_playing:
                self.start_alarm()
        else:
            if self.alarm_playing:
                self.stop_alarm()

    def start_alarm(self):
        pygame.mixer.music.load('mixkit-residential-burglar-alert-1656.wav')
        pygame.mixer.music.play(-1)  # Loop the sound
        self.alarm_playing = True

    def stop_alarm(self):
        pygame.mixer.music.stop()
        self.alarm_playing = False
    
    def yolov5_detection(self):
        video_path = self.video_entry.get()
        if video_path:
            SCRIPT = ["python", "C:\\Users\\rjdis\\jupyter\\Object Detection\\yolov5\\detect.py","--view-img", "--source", video_path, "--classes", "0"]
            s = subprocess.check_output(SCRIPT)
        self.run_detection_test()

    def frnn_detection(self):
        video_path = self.video_entry.get()
        if video_path:
            s = subprocess.run(["python", "C:\\Users\\rjdis\\jupyter\\Object Detection\\rnn\\detect_vid.py","--input", video_path ])  # Only detect persons
        self.run_detection_test()

    # Uncomment the following part and integrate with your friend's model
    # def start_detection(self):
    #     video_path = self.video_entry.get()
    #     if video_path:
    #         # Run YOLOv5 detection in a separate thread
    #         self.detection_thread = threading.Thread(target=self.run_detection, args=(video_path,))
    #         self.detection_thread.start()
    
    # def run_detection(self, video_path):
    #     cap = cv2.VideoCapture(video_path)
    #     while cap.isOpened():
    #         ret, frame = cap.read()
    #         if not ret:
    #             break
    #         # Use your model to detect people in the frame
    #         results = self.model(frame)
    #         people_count = len([d for d in results if d['class'] == 'person'])
    #         self.update_people_count(people_count)
    #         time.sleep(0.1)
    #     cap.release()

if __name__ == "__main__":
    app = PeopleDetectionApp()
    app.mainloop()
