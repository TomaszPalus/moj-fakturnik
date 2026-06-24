from app.services.telegram_service import (
    send_telegram_message
)

result = send_telegram_message(
    chat_id="6717058986",
    text="🚀 MojFakturnik działa!"
)

print(result)