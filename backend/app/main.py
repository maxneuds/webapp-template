from fastapi import FastAPI
from app.routes import demo
from app.config.config import settings
from app.db import database
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv("config/config.env")




# Define bootup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

# Create FastAPI app
app = FastAPI(lifespan=lifespan)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI MongoDB app!"}


