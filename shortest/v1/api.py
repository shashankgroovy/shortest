from http import HTTPStatus
from fastapi import APIRouter

from .mutator import EncoderPayload, Response
from .processor import decoder, encoder


router = APIRouter()


@router.get('', tags=['v1'])
@router.get('/', tags=['v1'])
def base() -> Response:
    """A base route to list the available endpoints"""
    route = {
        "/decode": "Endpoint to get original URL from shortened URL",
        "/encode": "Endpoint to shorten a URL"
    }

    return Response(
        status=HTTPStatus.OK,
        message=route
    )


@router.get('/decode', tags=['v1'])
def decode(shortened_url: str) -> Response:
    """Decodes a shortened URL and returns the original URL"""
    result = decoder(shortened_url)
    if result:
        return Response(
            status=HTTPStatus.OK,
            message=result
        )
    return Response(
        status=HTTPStatus.NOT_FOUND,
        message="Couldn't find that shortened URL"
    )


@router.post('/encode', tags=['v1'])
def encode(payload: EncoderPayload) -> Response:
    """Encode a URL and returns the shortened URL"""
    result = encoder(payload)
    return Response(
        status=HTTPStatus.OK,
        message=result
    )
