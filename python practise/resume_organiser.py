import os
from datetime import datetime
import shutil
from icecream import ic

def run():
    resume_folder = "C:\\Users\\rjdis\\OneDrive\\Desktop\\Material\\Self\\resume\\ordered resumes"
    try:
        for file_name in os.listdir(resume_folder):
            file_path = os.path.join(resume_folder, file_name)
            if os.path.isfile(file_path):
                dest = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m (%b)")
                res_container = os.path.join(resume_folder, dest)

                if os.path.exists(res_container):
                    print(f"folder {res_container} exists.")
                else:
                    os.makedirs(res_container)

                shutil.copy2(file_path, os.path.join(res_container, file_name))
                os.remove(file_path)
                
                
    except:
        pass


if __name__ == "__main__":
    run()