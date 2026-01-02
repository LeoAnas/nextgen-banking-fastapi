from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api.main import api_router
from .core.config import settings
from .core.logging import get_logger
from .core.db import init_db

logger=get_logger()

@asynccontextmanager
async def lifespan(app:FastAPI):
    logger.info("Starting Application")
    await init_db()
    yield
    logger.info("Application is Closing")
     
app=FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
) 

app.include_router(router=api_router,prefix=settings.API_V1_STR)
