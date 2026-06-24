from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "MojFakturnik"
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    TELEGRAM_BOT_TOKEN: str
    ENCRYPTION_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()