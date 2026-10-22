"""whoolib - unofficial Python client for the whoo mobile API.

The endpoint catalog and payload models were reconstructed from the
``app.whoo`` 0.140.0 Android APK (see ``docs/ENDPOINTS.md``).

Only use this library with your own account, in compliance with whoo's
Terms of Service and applicable privacy / anti-stalking laws.
"""

from .client import APP_VERSION, DEFAULT_BASE_URL, DEFAULT_USER_AGENT, WhooClient
from .exceptions import (
    APIError,
    AuthenticationError,
    HTTPError,
    NetworkError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    ServerError,
    ValidationError,
    WhooError,
)
from .models import MODEL_BY_NAME, MODEL_REGISTRY, Model

__version__ = "1.0.0"

__all__ = [
    "WhooClient",
    "Model",
    "MODEL_REGISTRY",
    "MODEL_BY_NAME",
    "WhooError",
    "NetworkError",
    "HTTPError",
    "APIError",
    "ValidationError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
    "APP_VERSION",
    "DEFAULT_BASE_URL",
    "DEFAULT_USER_AGENT",
    "__version__",
]
