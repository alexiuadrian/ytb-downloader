import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import threading

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError


def download_file(url, path, progress_bar, status_label):
    def progress_hook(d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded_bytes = d.get('downloaded_bytes', 0)
            if total_bytes:
                percent = int(downloaded_bytes * 100 / total_bytes)
                progress_bar["value"] = percent
                progress_bar.update()
        elif d['status'] == 'finished':
            progress_bar["value"] = 100
            progress_bar.update()
            status_label.config(text="Converting...")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'quiet': True,
        'noplaylist': False,
        'progress_hooks': [progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }

    try:
        status_label.config(text="⏬ Downloading...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text="Done")
    except DownloadError as e:
        status_label.config(text="Failed")
        print(f"Download error for {url}: {e}")

def start_downloads():
    urls = url_text.get("1.0", tk.END).strip().splitlines()
    path = path_entry.get()
    paths_arr = []

    for index in range(len(urls)):
        paths_arr.append(path + os.sep + str(index + 1))

    if not urls or not path:
        messagebox.showwarning("Input Error", "Please provide both URLs and a download path.")
        return

    for widget in progress_frame.winfo_children():
        widget.destroy()

    for index in range(len(urls)):
        url = urls[index]
        frame = tk.Frame(progress_frame)
        frame.pack(fill='x', padx=5, pady=5)

        label = tk.Label(frame, text=os.path.basename(url.split('?')[0])[:30] + "...", anchor="w", width=30)
        label.pack(side='left')

        progress = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
        progress.pack(side='left', padx=5)

        status = tk.Label(frame, text="Downloading...", width=15)
        status.pack(side='left')

        thread = threading.Thread(target=download_file, args=(url, paths_arr[index], progress, status))
        thread.start()

def browse_path():
    selected_path = filedialog.askdirectory()
    if selected_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, selected_path)

# GUI Setup
root = tk.Tk()
root.title("Multi File Downloader")
root.geometry("550x500")

tk.Label(root, text="Enter URLs (one per line):").pack(pady=5)
url_text = tk.Text(root, height=8, width=65)
url_text.pack(pady=5)

tk.Label(root, text="Save To Folder:").pack(pady=5)
path_frame = tk.Frame(root)
path_frame.pack(pady=5)

path_entry = tk.Entry(path_frame, width=45)
path_entry.pack(side=tk.LEFT, padx=(0, 5))
browse_button = tk.Button(path_frame, text="Browse", command=browse_path)
browse_button.pack(side=tk.LEFT)

tk.Button(root, text="Start Downloads", command=start_downloads).pack(pady=10)

progress_frame = tk.Frame(root)
progress_frame.pack(fill='both', expand=True, pady=10)

root.mainloop()
