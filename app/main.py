from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.routes_health import router as health_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    setup_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Include routers
    app.include_router(health_router, prefix=settings.api_v1_str)

    return app


app = create_app()
