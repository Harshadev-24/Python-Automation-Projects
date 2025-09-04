import yt_dlp
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",
            # 👈 change this to your ffmpeg\bin path
            "ffmpeg_location": r"C:\ffmpeg\ffmpeg-8.0-full_build\bin",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Video downloaded successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"📂 Selected folder: {folder}")
    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("🎬 Enter the YouTube video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("⬇️  Started download...")
        download_video(video_url, save_dir)
    else:
        print("⚠️ Invalid save location.")
