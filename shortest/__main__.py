from .app import bootload
from .config import get_settings


if __name__ == "__main__":
    import uvicorn

    settings = get_settings()
    uvicorn.run(bootload(), host=settings.app_host, port=int(settings.app_port))
