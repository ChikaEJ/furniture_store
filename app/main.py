from fastapi import FastAPI

from app.routers import router

app = FastAPI(title="FastApi app")

app.include_router(router)