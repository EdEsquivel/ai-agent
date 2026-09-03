from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_name: str = "gemma4:12b"
    ollama_host: str = "http://127.0.0.1:11434"
    max_concurrent_ai_requests: int = 1

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()