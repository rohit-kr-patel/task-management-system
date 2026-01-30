from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.include_router(
        health_router,
        prefix=settings.api_v1_prefix
    )

    app.include_router(
        auth_router,
        prefix=settings.api_v1_prefix
    )

    return app


app = create_app()
