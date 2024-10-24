import os

import yt_dlp

# List of YouTube video URLs
with open(file='PythonToday_SQL_Tutorial/sorted_link_video.txt', mode='r') as file:
    source = file.read().split()

    output_dir_name = f"{file.name.split('/')[0]}/{file.name.split('/')[0]}_video"

# Options for yt-dlp (download highest quality by default)
ydl_opts = {
    'format': 'best',  # 'best' downloads the highest quality available
    'outtmpl': os.path.join(output_dir_name, '%(title)s.%(ext)s'),  # Save with video title as filename
}

# Function to download a video
def download_video(url):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Iterate over the list and download each video
for video_url in source:
    download_video(video_url)

