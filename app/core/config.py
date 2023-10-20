from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Веб-сервис получения вопросов викторины"
    description: str = "Асинхронный веб-сервис"
    postgres_db: str = "fastapi"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    db_host: str = "db"
    db_port: str = "5432"
    database_url: str = (
        "postgresql+asyncpg://"
        f"{postgres_user}:{postgres_password}@{db_host}:{db_port}/"
        f"{postgres_db}"
    )

    public_api_url: str = "https://jservice.io/api/"

    class Config:
        env_file = ".env"


settings = Settings()
