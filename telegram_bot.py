import requests
import config

def send_message(msg):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.TELEGRAM_CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)
