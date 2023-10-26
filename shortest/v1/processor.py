import hashlib
import logging
from typing import Optional

from redis.exceptions import ConnectionError

from shortest.config import get_settings
from shortest.utils.cache import Cache
from .mutator import EncoderPayload

# Initalize the cache and log
cache = Cache()
log = logging.getLogger(__name__)


def _encode(url: str, *, offset: int = 0, length: int = 5) -> str:
    """Encodes a given url string using MD5 and returns a hex of
    given length

    Args:
        url: A given url to encode
        offset: Offset the hash bits
        length: Length of hash to be returned

    Returns:
        str: A hex digest of given length
    """
    hex = hashlib.md5(url.encode()).hexdigest()
    return hex[offset: (offset + length)]


def encoder(payload: EncoderPayload) -> Optional[str]:
    """Returns a shortened url

    Args:
        payload: An Encoder payload
    Retuns:
        str: Shortened URL computed using MD5 hash
    """

    settings = get_settings()

    # Proceed with encoding the URL
    hex = _encode(payload.source_url)
    url = f"{settings.base_url}/{hex}"

    try:
        # Cache check
        stored_url = cache.get(url) or None
        if stored_url:
            if stored_url == payload.source_url:
                return url

            # Conflict! Recompute hash with offset
            hex = _encode(payload.source_url, offset=8)
            url = f"{settings.base_url}/{hex}"

        # Populate cache
        cache.set(url, payload.source_url)
        return url
    except ConnectionError as err:
        log.warn(
            "Whoops! Unable to connect to Redis."
            " Make sure Redis is up and runnning"
        )
        raise err


def decoder(shortened_url: str) -> Optional[str]:
    """Returns original URL upon decoding shortened URL

    Args:
        shortened_url: A shortened URL
    Retuns:
        str|None: Original URL or None
    """

    try:
        # Cache check
        stored_url = cache.get(shortened_url) or None
        return stored_url.decode() if stored_url else None
    except ConnectionError as err:
        log.warn(
            "Whoops! Unable to connect to Redis."
            " Make sure Redis is up and runnning"
        )
        raise err
