from pydantic_settings import BaseSettings, SettingsConfigDict

# конфиг для подключения к БД
class Settings(BaseSettings):
	DB_HOST: str
	DB_PORT: int
	DB_NAME: str
	DB_USER: str
	DB_PASS: str
	
	def __repr__(self) -> str:
		return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"		
	
	model_config = SettingsConfigDict(env_file=".env")