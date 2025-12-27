from fastapi import APIRouter
from backend.app.core.logging import get_logger

router = APIRouter()

logger = get_logger()


@router.get("/")
def home():
    logger.info("accessed home page ")
    logger.debug("accessed home page ")
    logger.warning("accessed home page ")
    logger.error("accessed home page ")
    logger.exception("accessed home page ")
    return {"Hello": "Banking API"}
