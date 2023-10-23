from .app import app
from .config import get_settings


if __name__ == "__main__":
    import uvicorn

    settings = get_settings()
    uvicorn.run(app, host=settings.app_host, port=int(settings.app_port))
