"""
OfferService methods
Offer management endpoints
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class OfferService:
    """OfferService mixin for KworkClient"""

    async def get_offer(self, id: int) -> Dict[str, Any]:
        """Get offer by ID"""
        params = {"id": id}
        return await self._request("/offer", params=params)

    async def get_offers(self, page: int = 1) -> Dict[str, Any]:
        """Get offers"""
        params = {"page": page}
        return await self._request("/offers", params=params)

    async def delete_offer(self, id: int) -> Dict[str, Any]:
        """Delete offer"""
        params = {"id": id}
        return await self._request("/deleteOffer", params=params)
