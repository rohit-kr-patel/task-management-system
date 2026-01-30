from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    api_v1_prefix: str

    class Config:
        env_file = ".env"


settings = Settings()
