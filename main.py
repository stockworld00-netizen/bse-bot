import time
from bse_fetcher import get_latest_announcements
from db import is_duplicate
from telegram_bot import send_message
from categorizer import categorize_announcement
import config

def job():
    announcements = get_latest_announcements()
    for ann in announcements:
        unique_id = ann["ATTACHMENTNAME"]
        if is_duplicate(unique_id):
            continue

        headline = ann["HEADLINE"]
        company = ann.get("SLONGNAME", "Unknown Company")

        category, emoji = categorize_announcement(headline)

        message = f"""
{emoji} *{category}*

🏢 {company}
📰 {headline}

⏱ Source: BSE
#BSE #StockMarket
"""
        send_message(message)

if __name__ == "__main__":
    while True:
        job()
        time.sleep(config.CHECK_INTERVAL)
