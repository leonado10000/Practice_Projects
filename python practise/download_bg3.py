
import os
import requests
from tqdm import tqdm

# CONFIGURATION
URLS_FILE = "C:\\Users\\rjdis\\OneDrive\\Documents\\GitHub\\Practice_Projects\\python practise\\urls.txt" # file containing all the download URLs
DOWNLOAD_DIR = "C:\\Users\\rjdis\\Downloads\\BG3" # change this to your desired folder

# Ensure download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Read all URLs from the file
with open(URLS_FILE, 'r') as f:
    urls = [line.strip() for line in f if line.strip()]

# Download each file one-by-one
for url in urls:
    try:
        filename = url.split('#')[-1] or url.split('/')[-1]
        filepath = os.path.join(DOWNLOAD_DIR, filename)

        if os.path.exists(filepath):
            print(f"[SKIP] Already exists: {filename}")
            continue

        print(f"[START] Downloading: {filename}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))
        with open(filepath, 'wb') as file, tqdm(
            desc=filename,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content():
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))

        print(f"[DONE] Completed: {filename}\n")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to download {url}\nReason: {e}\n")
