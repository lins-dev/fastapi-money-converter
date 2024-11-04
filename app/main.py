from fastapi import FastAPI
from .conversions import routers as converions_routers
import os
from dotenv import load_dotenv

app = FastAPI()
app.include_router(converions_routers.router)

# Load .env file
load_dotenv()

ALPHA_VANTAGE_API = os.getenv("ALPHA_VANTAGE_API")

@app.get("/")
async def root():
    return {"message": "Hello World!"}
