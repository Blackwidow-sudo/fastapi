from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Awesome API'
    api_key: str
    api_key_header: str = 'X-API-KEY'

    # Load .env variables, but ignore undeclared ones
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()