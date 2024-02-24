import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
from typing import List


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    APP_NAME: str = os.environ.get("APP_NAME", "Currency")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    SQL_HOST: str = os.environ.get("SQL_HOST", "localhost")
    SQL_USER: str = os.environ.get("SQL_USER", "root")
    SQL_PASSWORD: str = os.environ.get("SQL_PASSWORD", "password")
    SQL_PORT: str = os.environ.get("SQL_PORT", 5432)
    SQL_DB: str = os.environ.get("SQL_DB", "currency_db")
    DATABASE_URI: str = (
        f"postgresql+asyncpg://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DB}"
    )

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "secret")
    SOURCE_URL: str = os.environ.get("SOURCE_URL")
    API_KEY: str = os.environ.get("API_KEY")
    CURRENCY_NAMES: dict = {'EUR': 'Euro', 'USD': 'US Dollar', 'JPY': 'Japanese Yen', 'BGN': 'Bulgarian Lev', 'CZK': 'Czech Republic Koruna', 'DKK': 'Danish Krone', 'GBP': 'British Pound Sterling', 'HUF': 'Hungarian Forint', 'PLN': 'Polish Zloty', 'RON': 'Romanian Leu', 'SEK': 'Swedish Krona', 'CHF': 'Swiss Franc', 'ISK': 'Icelandic Króna', 'NOK': 'Norwegian Krone', 'HRK': 'Croatian Kuna', 'RUB': 'Russian Ruble', 'TRY': 'Turkish Lira', 'AUD': 'Australian Dollar', 'BRL': 'Brazilian Real', 'CAD': 'Canadian Dollar', 'CNY': 'Chinese Yuan', 'HKD': 'Hong Kong Dollar', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli New Sheqel', 'INR': 'Indian Rupee', 'KRW': 'South Korean Won', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'NZD': 'New Zealand Dollar', 'PHP': 'Philippine Peso', 'SGD': 'Singapore Dollar', 'THB': 'Thai Baht', 'ZAR': 'South African Rand'}
    CURRENCY_CODES: List = os.environ.get("CURRENCY_CODE").split(" ")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
