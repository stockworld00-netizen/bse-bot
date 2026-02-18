import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
CHECK_INTERVAL = 60  # seconds
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # optional if AI parsing used
