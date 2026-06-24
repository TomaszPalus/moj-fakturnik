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
    
def delete_channel(
    db,
    channel_id: int,
    user_id: int
):
    channel = (
        db.query(NotificationChannel)
        .filter(NotificationChannel.id == channel_id)
        .filter(NotificationChannel.user_id == user_id)
        .first()
    )

    if not channel:
        return False

    db.delete(channel)
    db.commit()

    return True

def toggle_channel(
    db,
    channel_id: int,
    user_id: int
):
    channel = (
        db.query(NotificationChannel)
        .filter(NotificationChannel.id == channel_id)
        .filter(NotificationChannel.user_id == user_id)
        .first()
    )

    if not channel:
        return None

    channel.is_active = not channel.is_active

    db.commit()
    db.refresh(channel)

    return channel