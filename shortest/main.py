from http import HTTPStatus
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
@app.get("/health")
async def health():
    return {'status': HTTPStatus.OK}
