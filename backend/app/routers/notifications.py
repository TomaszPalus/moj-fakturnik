from fastapi import APIRouter
from fastapi import Depends

from app.dependencies import get_db
from app.dependencies import get_current_user

from app.schemas.notification_channel import (
    NotificationChannelCreate
)

from app.services.notification_service import (
    create_notification_channel,
    get_user_channels,
    get_active_user_channels
)

from app.services.telegram_service import send_telegram_message

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)


@router.post("/channel")
def add_channel(
    data: NotificationChannelCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_notification_channel(
        db=db,
        user_id=current_user.id,
        channel_type=data.type,
        destination=data.destination
    )


@router.get("/channel")
def list_channels(
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_user_channels(
        db,
        current_user.id
    )
    
@router.post("/test")
def test_notifications(
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    channels = get_active_user_channels(
        db=db,
        user_id=current_user.id
    )

    sent = []

    for channel in channels:
        if channel.type == "telegram":
            result = send_telegram_message(
                chat_id=channel.destination,
                text="✅ Test MojFakturnika\n\nJeżeli widzisz tę wiadomość, powiadomienia działają."
            )

            sent.append({
                "channel_id": channel.id,
                "type": channel.type,
                "result": result
            })

    return {
        "sent": sent
    }