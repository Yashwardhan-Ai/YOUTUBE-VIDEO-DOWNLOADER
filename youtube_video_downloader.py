from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os

def download_video(url,save_path):
  try:
    yt = YouTube(url)
    streams=yt.streams.filter(progressive = True,file_extension="mp4")
    highest_res_stream = streams.get_highest_resolution()
    filename = highest_res_stream.default_filename
    full_save_path = os.path.join(save_path, filename)
    highest_res_stream.download(output_path=save_path, filename=filename)
    print("Video downloaded")
  except Exception as e:
    print (e)
url = "https://www.youtube.com/watch?v=0sxjHL6TORw"
save_path = r"D:\\Python VS CODE\\Twenty one days of twenty one projects"

download_video(url,save_path)

