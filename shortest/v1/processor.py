import hashlib

from shortest.config import get_settings
from .mutator import Payload


def _encode(url: str, length: int = 5, offset: int = 0) -> str:
    '''Encodes a given url string using md5 and returns a hex of
    given length

    Args:
        url: A given url to encode
        length: Length of hash to be returned
        offset: Offset the hash bits

    Returns:
        str: A hex digest of given length
    '''
    hex = hashlib.md5(url.encode()).hexdigest()
    return hex[offset:length]


def encoder(payload: Payload) -> str:
    '''Encodes a given url and returns it'''

    settings = get_settings()
    if payload.custom_hex:
        payload.custom_hex
        return f'{settings.base_url}/{payload.custom_hex}'

    # Proceed with encoding the url
    hex = _encode(payload.source_url)
    return f'{settings.base_url}/{hex}'
