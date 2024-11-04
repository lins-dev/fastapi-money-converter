import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Carrega automaticamente o arquivo .env
load_dotenv()

class Settings(BaseSettings):
    alpha_vantage_api: str = os.getenv("ALPHA_VANTAGE_API")
    alpha_vantage_api_v2: str = os.getenv("ALPHA_VANTAGE_API_V2")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()