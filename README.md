YouTube Summarizer Telegram Bot 

Table of Contents

Project Overview

Features

Architecture

Setup Instructions

Usage

Error Handling

Repository Structure

Project Overview

This project implements a Telegram bot that summarizes YouTube videos.
The bot helps users:

Quickly get the key content from long YouTube videos

Receive a concise and structured summary

Currently, the bot does not support Q&A or multi-language, focusing solely on transcript extraction and summarization.

Features

Accepts a YouTube link from the user

Fetches transcript automatically using yt-dlp

Cleans the transcript text

Generates a structured summary

Replies to the user with the summary via Telegram

Architecture
High-level Flow
[User sends YouTube URL] 
        │
        ▼
[Bot fetches transcript using yt-dlp]
        │
        ▼
[Clean transcript text]
        │
        ▼
[Generate summary using local summarizer]
        │
        ▼
[Send summary to user via Telegram]
Components

Telegram Bot – Handles user messages and replies

Transcript Handler – Downloads and cleans subtitles

Summarizer – Generates concise summaries from transcripts

Setup Instructions
Prerequisites

Python 3.11+

Telegram bot token (via BotFather)

ffmpeg installed and added to PATH

yt-dlp library

Install Dependencies
pip install python-telegram-bot yt-dlp gensim
Environment Variables

Create a .env file in the project folder:

TELEGRAM_TOKEN=<8703179608:AAGgWm8jjcg2gBIqbs_qzbWWdGrYQQd0s9Q>
Run Bot
python bot.py
Usage

User sends a YouTube link:

https://www.youtube.com/watch?v=dQw4w9WgXcQ

Bot responds with:

🎥 Video Title: Never Gonna Give You Up  
📌 Summary: The video/song expresses themes of loyalty, love, and commitment. The singer emphasizes unwavering support and assures the partner that they will never be let down. The repetition highlights sincerity and emotional connection.
Error Handling

Invalid YouTube URL → Bot replies “Invalid video link.”

Transcript unavailable → Bot replies “Transcript not available for this video.”

Long videos → Transcript cleaned and summarized

Network errors → Graceful error messages printed in bot logs

Repository Structure
eywa_bot/
├─ bot.py                # Main Telegram bot
├─ transcript.py         # Fetch & clean YouTube transcripts
├─ llm.py                # Summarization logic
├─ .env
└─ README.md
