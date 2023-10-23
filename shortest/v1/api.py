from http import HTTPStatus
from fastapi import APIRouter, HTTPException

from .mutator import EncoderPayload, Response
from .processor import CACHE, decoder, encoder


router = APIRouter()


@router.get("/list", tags=["v1"])
async def list_routes() -> Response:
    """Route to list all available shortlinks"""

    return Response(status=HTTPStatus.OK, message=CACHE)


@router.get("/decode", tags=["v1"])
async def decode(shortened_url: str) -> Response:
    """Decodes a shortened URL and returns the original URL"""

    result = decoder(shortened_url)
    if result:
        return Response(status=HTTPStatus.OK, message=result)

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="Couldn't find that shortened URL",
    )


@router.post("/encode", tags=["v1"])
async def encode(payload: EncoderPayload) -> Response:
    """Encode a URL and returns the shortened URL"""
    result = encoder(payload)
    return Response(status=HTTPStatus.OK, message=result)
