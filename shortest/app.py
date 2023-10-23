from http import HTTPStatus
from fastapi import FastAPI

from shortest.v1.api import router as v1_router

app = FastAPI()
app.include_router(v1_router, prefix="/v1")


@app.get("/")
@app.get("/health")
async def health():
    return {"status": HTTPStatus.OK}
