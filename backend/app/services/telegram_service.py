import requests

from app.core.config import settings


def send_telegram_message(
    chat_id: str,
    text: str
):
    url = (
        f"https://api.telegram.org/bot"
        f"{settings.TELEGRAM_BOT_TOKEN}"
        f"/sendMessage"
    )

    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": text
        }
    )

    return response.json()