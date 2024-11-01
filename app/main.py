from fastapi import FastAPI
from .conversions import routers as converions_routers

app = FastAPI()
app.include_router(converions_routers.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}
