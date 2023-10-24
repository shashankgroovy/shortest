from http import HTTPStatus
from fastapi import APIRouter, HTTPException

from .mutator import EncoderPayload, Response
from .processor import decoder, encoder


router = APIRouter()


@router.get("/decode", tags=["v1"])
async def decode(shortened_url: str) -> Response:
    """Decodes a shortened URL and returns the original URL"""

    try:
        result = decoder(shortened_url)
        if result:
            return Response(status=HTTPStatus.OK, message=result)

        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Couldn't find that shortened URL",
        )
    except Exception:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail="Something went wrong!",
        )


@router.post("/encode", tags=["v1"])
async def encode(payload: EncoderPayload) -> Response:
    """Encode a URL and returns the shortened URL"""
    try:
        result = encoder(payload)
        if result:
            return Response(status=HTTPStatus.OK, message=result)

    except Exception:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail="Something went wrong!",
        )
