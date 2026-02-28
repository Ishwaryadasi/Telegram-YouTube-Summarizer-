import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_summary(transcript):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "youtube-summary-bot"
        }

        data = {
            "model": "openai/gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": f"Summarize this transcript clearly:\n\n{transcript[:4000]}"
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data, timeout=30)

        print("STATUS CODE:", response.status_code)

        if response.status_code != 200:
            print("ERROR RESPONSE:", response.text)
            return "API Error. Please check your OpenRouter API key or credits."

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("REAL ERROR:", e)
        return "Summary generation failed."