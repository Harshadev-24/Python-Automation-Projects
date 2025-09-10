# Python-Automation-Projects

A collection of beginner-friendly automation projects written in Python. These scripts demonstrate how Python can be used to automate everyday tasks like managing clipboard snippets, sending emails, and downloading YouTube videos.

# 🐍 Python Automation Projects

This repository contains **three Python automation projects** that demonstrate how to automate simple but useful tasks with Python:

1. **MultiClipboard Manager** – store and retrieve multiple clipboard snippets.  
2. **Email Sender** – send emails securely using Gmail SMTP.  
3. **YouTube Downloader** – download YouTube videos in the highest available resolution (1080p/2K/4K) with yt-dlp and FFmpeg.
4. **Python Log Parser** -  This script combines all the steps. It reads app.log, applies the regex, and prints the structured data.

---

## 📂 Project 1: MultiClipboard Manager (`multiclipboard.py`)

Manage multiple clipboard snippets using a JSON file.

### ✨ Features
- Save custom text with a key.
- Load text back into your clipboard.
- List all saved snippets.

### ⚡ Requirements
- Python 3.8+
- [pyperclip](https://pypi.org/project/pyperclip/)

```bash
pip install pyperclip
```

▶️ Usage
# Save a snippet
```bash
python multiclipboard.py save note1 "Python is awesome"
```

# Load a snippet into clipboard
```bash
python multiclipboard.py load note1
```

# List all saved snippets
```bash
python multiclipboard.py list
```

Snippets are stored in clipboard.json

## 📂 Project 2: Email Sender (`sending_email.py`)

Send emails directly using Python’s `smtplib` and Gmail’s SMTP server.

### ✨ Features
- Secure SSL connection.  
- Uses Gmail’s SMTP.  
- Requires Gmail **App Password** (not your normal password).  

### ⚡ Requirements
- Python 3.8+  
- Gmail account with **2-Step Verification** enabled.  

### 🔐 Setup
1. Enable **2-Step Verification** on your Gmail account.  
2. Generate a **16-character App Password**.  
3. Replace the `password` field in `sending_email.py` with your App Password.  

### ▶️ Usage
```bash
python sending_email.py
```

## 📂 Project 3: YouTube Downloader (`youtube_downloader.py`)

Download YouTube videos in the highest available quality (1080p, 2K, 4K) using **yt-dlp**.  
Requires **FFmpeg** for merging video + audio.

### ✨ Features
- Highest resolution available (`bestvideo+bestaudio`).  
- Auto-merges video + audio into MP4.  
- Choose download folder via Tkinter file dialog.  

### ⚡ Requirements
- Python 3.8+  
- [yt-dlp](https://pypi.org/project/yt-dlp/)  
- [FFmpeg](https://ffmpeg.org/) installed and added to PATH.  

Install yt-dlp:
```bash
pip install yt-dlp
```

## 📂 Project 4: Python Log Parser (`log_parsing.py`)

A simple yet powerful Python script for parsing structured log files using regular expressions. This tool reads log entries, extracts key information like timestamps, log levels, and messages, and converts them into a structured format (a list of dictionaries) for easy analysis.

## Features ✨
Pattern-Based Parsing: Uses Python's re module for flexible and powerful log matching.

Structured Output: Converts unstructured log lines into a list of dictionaries (JSON).

Error Resilient: Ignores and reports malformed or non-matching log lines instead of crashing.

Memory Efficient: Reads the log file line-by-line, making it suitable for large files.

Easily Customizable: Designed for easy modification of the file path and regex pattern to fit your specific needs.

## Prerequisites
Python 3.6+ (due to the use of f-strings)

No external libraries are needed. The script uses the built-in ``` re ``` and ``` json ``` modules.

## Usage 🚀
Place the Files: Save the script as log_parsing.py. Place your log file (e.g., app.log) in the same directory.

Configure the Script: Open log_parsing.py and modify the file_path variable inside the if __name__ == "__main__": block to point to your log file.

```bash

python log_parsing.py
```
View the Output: The script will print the parsed data to the console in a pretty-printed JSON format. It will also notify you of any lines it skipped.
