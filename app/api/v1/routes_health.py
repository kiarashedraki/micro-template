from fastapi import APIRouter
from typing import Dict, Any
import datetime

router = APIRouter()


@router.get("/health", response_model=Dict[str, Any])
async def health_check():
    """Health check endpoint to verify service is running."""
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "service": "fastapi-blueprint"
    }
