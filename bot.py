import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from transcript import get_transcript
from llm import generate_summary

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    youtube_url = update.message.text.strip()

    await update.message.reply_text("Fetching transcript...")
    transcript = get_transcript(youtube_url)

    if not transcript:
        await update.message.reply_text("Transcript not available for this video.")
        return

    await update.message.reply_text("Generating summary...")
    summary = generate_summary(transcript)
    await update.message.reply_text(summary)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()