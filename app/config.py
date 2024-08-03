from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	MONGO_URL: str
	REDIS_URL: str

	model_config = SettingsConfigDict(env_file='.env')


settings = Settings()