from http import HTTPStatus
from fastapi import FastAPI

from shortest.v1.api import router as v1_router


def bootload() -> FastAPI:
    app = FastAPI()

    # Setup routes
    app = bootload_routes(app)
    return app


def bootload_routes(app: FastAPI) -> FastAPI:
    @app.get("/")
    @app.get("/health")
    async def health():
        return {"status": HTTPStatus.OK}

    # Load API routes
    app.include_router(v1_router, prefix="/v1")

    return app
