from typing import Any
from http import HTTPStatus

from pydantic import BaseModel


class EncoderPayload(BaseModel):
    """Payload for shortening a URL"""

    source_url: str


class Response(BaseModel):
    """A default response class"""

    status: HTTPStatus
    message: Any
