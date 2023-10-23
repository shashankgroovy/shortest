from .app import app


if __name__ == "__main__":
    import os
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", "8000")

    uvicorn.run(app, host=host, port=int(port))
