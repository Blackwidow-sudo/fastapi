from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

from .config import settings


header_scheme = APIKeyHeader(name=settings.api_key_header)


def validate_api_key(client_key: str = Security(header_scheme)):
    if client_key != settings.api_key:
        raise HTTPException(401, 'Unauthorized')
    return client_key
