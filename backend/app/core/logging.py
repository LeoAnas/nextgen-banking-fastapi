from loguru import logger
from pathlib import Path
from .config import settings
logger.remove()  # to remove the default logger

LOG_DIR=Path(__file__).parent / "logs"
LOG_DIR.mkdir( exist_ok=True) # if the file already exists do nothing just use it


# level <8 so all the levels take the same spacing so they are all aligned
LOG_FORMAT = (
    "{time:YYYY-MM-DD HH:mm:ss.SSS} | "
    "{level:<8} | "
    "{name}:{function}:{line} - "
    "{message}"
)

logger.add(sink=LOG_DIR/"debug.log",
           format=LOG_FORMAT,
           level="DEBUG" if settings.ENVIRONMENT=="local" else "INFO",
           filter= lambda record: record["level"].no <= logger.level("WARNING").no,
           rotation="10MB",
           retention="30 days",
           compression="zip",
           )

# Never use diagnose=True in Production
logger.add(sink=LOG_DIR/"error.log",
           format=LOG_FORMAT,
           level="ERROR",
           rotation="10MB",
           retention="30 days",
           compression="zip",
           backtrace=True,
           diagnose=True if not settings.ENVIRONMENT=="production" else False
           ) 


def get_logger():
    return logger




