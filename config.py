from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):
    DB_USER: str = ''
    DB_PASSWORD: str = ''
    DB_HOST: str = ''
    DB_PORT: str = ''
    DB_NAME: str = ''
    DB_MODE: Literal["SQLITE", "POSTGRESQL"]
    

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8")

    def get_db_url(self):
        db_name = self.DB_NAME or "books.db"
        check = all((self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_PORT,self.DB_NAME,self.DB_MODE))
        if check and self.DB_MODE == "POSTGRESQL":
            database_url = (f'postgresql+asyncpg://'
                            f'{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')
        else:
            path = BASE_DIR / f'{db_name}'
            database_url = f"sqlite+aiosqlite:///{path}"
        return database_url
    

settings = Settings()