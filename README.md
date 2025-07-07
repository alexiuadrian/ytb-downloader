# Multi File MP3 Downloader (GUI)

A simple Python application with a graphical interface that downloads multiple audio files (MP3) from URLs using **yt-dlp** and converts them to high-quality MP3 files. Supports live download progress for each file.

---

## Features

- ✅ Download multiple files at once
- ✅ Convert to **MP3** using the best audio quality
- ✅ Show progress bars for each download
- ✅ Friendly GUI built with **Tkinter**
- ✅ Save files to a custom folder
- ✅ Uses `yt-dlp` Python API (no command line needed)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/alexiuadrian/ytb-downloader.git
cd ytb-downloader

```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

Then install the required packages:

```bash
pip install -r requirements.txt

```

---

### 3. Install FFmpeg

This app needs **FFmpeg** installed and available in your PATH.

### Windows:

- Download from: https://www.gyan.dev/ffmpeg/builds/
- Extract and add the `bin/` folder to your PATH environment variable.

### macOS:

```bash
brew install ffmpeg

```

### Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg

```

Verify installation:

```bash
ffmpeg -version

```

---

## Usage

Run the application:

```bash
python main.py

```

- Paste one or more URLs (each on a new line).
- Select the destination folder.
- Click **Start Downloads**.
- Progress bars will show for each download.

---

## 🔧 Requirements

- Python 3.8+
- yt-dlp
- FFmpeg
- Tkinter (bundled with Python)

See [`requirements.txt`](https://github.com/alexiuadrian/ytb-downloader/blob/main/requirements.txt).

---

## ⚠️ Notes

- Make sure the URLs point to downloadable content supported by yt-dlp.
- Some sites may require additional login/authentication, which is not handled in this simple app.

---

## 📄 License

MIT License. Feel free to use and modify.