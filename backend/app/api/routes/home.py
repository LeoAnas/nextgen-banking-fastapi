from fastapi import APIRouter
from backend.app.core.logging import get_logger

router = APIRouter()

logger = get_logger()


@router.get("/")
def home():
    return {"Hello": "Banking API"}
