import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Blog Service"
    base_url_prefix: str = "/api/v1"
    es_host: str = os.getenv("ELASTICSEARCH_HOST")
    rabbitmq_host: str = os.getenv("RABBITMQ_HOST")


settings = Settings()
