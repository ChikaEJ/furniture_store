from fastapi import FastAPI

from app.routers import router

app = FastAPI(title="Furniture Store")

app.include_router(router)