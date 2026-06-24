from app.models.notification_channel import NotificationChannel


def create_notification_channel(
    db,
    user_id: int,
    channel_type: str,
    destination: str
):
    channel = NotificationChannel(
        user_id=user_id,
        type=channel_type,
        destination=destination
    )

    db.add(channel)
    db.commit()
    db.refresh(channel)

    return channel


def get_user_channels(
    db,
    user_id: int
):
    return (
        db.query(NotificationChannel)
        .filter(NotificationChannel.user_id == user_id)
        .all()
    )
    
def get_active_user_channels(
    db,
    user_id: int
):
    return (
        db.query(NotificationChannel)
        .filter(NotificationChannel.user_id == user_id)
        .filter(NotificationChannel.is_active == True)
        .all()
    )