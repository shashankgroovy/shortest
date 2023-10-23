from http import HTTPStatus
from fastapi import APIRouter

from .mutator import Payload, Response
from .processor import encoder


router = APIRouter()


@router.get('', tags=['v1'])
@router.get('/', tags=['v1'])
def base() -> Response:
    """A base route to list the available endpoints"""
    route = {
        "/encode": "Endpoint to shorten a URL",
        "/decode": "Endpoint to get original URL from shortened URL"
    }
    return Response(
        status=HTTPStatus.OK,
        message=route
    )


@router.post('/encode', tags=['v1'])
def encode(payload: Payload) -> Response:
    """Encode a URL and returns the shortened URL"""
    result = encoder(payload)
    return Response(
        status=HTTPStatus.OK,
        message=result
    )


@router.get('/decode', tags=['v1'])
def decode() -> Response:
    """Decodes a shortened URL and returns the original URL"""
    return Response(
        status=HTTPStatus.OK,
        message="Decoder api route"
    )
