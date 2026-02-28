import yt_dlp
import os

def get_transcript(url):
    try:
        ydl_opts = {
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["en"],
            "subtitlesformat": "vtt",
            "outtmpl": "temp",
            "quiet": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        # Find downloaded .vtt file
        for file in os.listdir():
            if file.endswith(".vtt"):
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                os.remove(file)  # clean up
                return clean_vtt(content)

        return ""

    except Exception as e:
        print("Transcript Error:", e)
        return ""


def clean_vtt(content):
    lines = content.splitlines()
    text = []

    for line in lines:
        if "-->" not in line and line.strip() and not line.startswith("WEBVTT"):
            text.append(line.strip())

    return " ".join(text)