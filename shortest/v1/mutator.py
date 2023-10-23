from typing import Any, Optional
from http import HTTPStatus

from pydantic import BaseModel, Field


class Payload(BaseModel):
    '''Payload for shortening a URL'''
    source_url: str
    custom_hex: Optional[str] = Field(
        default=None,
        max_length=10,
        description='A custom url key to be used instead of hash'
    )


class Response(BaseModel):
    '''A default response class'''
    status: HTTPStatus
    message: Any
