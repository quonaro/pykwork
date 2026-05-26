"""
Kwork API Library
Python library for working with Kwork API
"""

from .client import KworkClient
from .exceptions import KworkAPIError, KworkAuthError, KworkRequestError
from .sync_client import KworkSyncClient

__version__ = "2.0.0"
__all__ = [
    "KworkClient",
    "KworkSyncClient",
    "KworkAPIError",
    "KworkAuthError",
    "KworkRequestError",
]
