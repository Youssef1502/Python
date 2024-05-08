#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python Script to download video from Youtube
================================================================================'''

from pytube import YouTube

def download_video(url, path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(path)
        print("Download completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# YouTube video URL
url = "https://www.youtube.com/0000000000000000000000"  # Example URL, replace it with your video URL

# Path to save the downloaded video
path = "./"  # Current directory, you can change it to your desired directory

download_video(url, path)
