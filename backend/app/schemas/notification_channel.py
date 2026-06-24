from pydantic import BaseModel


class NotificationChannelCreate(BaseModel):
    type: str
    destination: str


class NotificationChannelResponse(BaseModel):
    id: int
    type: str
    destination: str
    is_active: bool

    class Config:
        from_attributes = True