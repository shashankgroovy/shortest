import hashlib

from shortest.config import get_settings
from .mutator import EncoderPayload

CACHE: dict[str, str] = {}


def _encode(url: str, *, offset: int = 0, length: int = 5) -> str:
    '''Encodes a given url string using MD5 and returns a hex of
    given length

    Args:
        url: A given url to encode
        offset: Offset the hash bits
        length: Length of hash to be returned

    Returns:
        str: A hex digest of given length
    '''
    hex = hashlib.md5(url.encode()).hexdigest()
    return hex[offset:(offset+length)]


def encoder(payload: EncoderPayload) -> str:
    '''Returns a shortened url

    Args:
        payload: An Encoder payload
    Retuns:
        str: Shortened URL computed using MD5 hash
    '''

    settings = get_settings()

    # Proceed with encoding the URL
    hex = _encode(payload.source_url)
    url = f'{settings.base_url}/{hex}'

    # Cache check
    if url in CACHE:
        if CACHE[url] == payload.source_url:
            return url

        # Conflict! Recompute hash with offset
        hex = _encode(payload.source_url, offset=8)
        url = f'{settings.base_url}/{hex}'

    # Add to cache
    CACHE[url] = payload.source_url
    return url


def decoder(shortened_url: str) -> str | None:
    '''Returns original URL upon decoding shortened URL

    Args:
        shortened_url: A shortened URL
    Retuns:
        str|None: Original URL or None
    '''

    # Cache check
    if shortened_url in CACHE:
        return CACHE[shortened_url]

    return None
