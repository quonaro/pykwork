"""
ExchangeService methods
Project exchange endpoints
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class ExchangeService:
    """ExchangeService mixin for KworkClient"""

    async def get_my_wants(self, page: int = 1, want_status_id: int = 0) -> Dict[str, Any]:
        """Get archived projects"""
        params = {"page": page, "want_status_id": want_status_id}
        return await self._request("/myWants", params=params)

    async def delete_offer(self, offer_id: int) -> Dict[str, Any]:
        """Delete offer"""
        params = {"id": offer_id}
        return await self._request("/deleteOffer", params=params)

    async def delete_want(self, want_id: int) -> Dict[str, Any]:
        """Delete want"""
        params = {"id": want_id}
        return await self._request("/deleteWant", params=params)

    async def get_exchange_info(self) -> Dict[str, Any]:
        """Get exchange info"""
        return await self._request("/exchangeInfo", params={})

    async def get_favorite_categories(self) -> Dict[str, Any]:
        """Get favorite categories"""
        return await self._request("/favoriteCategories", params={})

    async def get_offer(self, offer_id: int) -> Dict[str, Any]:
        """Get specific offer"""
        params = {"id": offer_id}
        return await self._request("/offer", params=params)

    async def get_wants_count(
        self,
        categories: str = "",
        attributes: str = "",
        price_from: int = 0,
        price_to: int = 0,
        hiring_from: int = 0,
        offers: str = "",
    ) -> Dict[str, Any]:
        """Get wants count"""
        params = {
            "categories": categories,
            "attributes": attributes,
            "price_from": price_from,
            "price_to": price_to,
            "hiring_from": hiring_from,
            "offers": offers,
        }
        return await self._request("/getWantsCount", params=params)

    async def get_project(self, project_id: int) -> Dict[str, Any]:
        """Get project details by ID

        Args:
            project_id: Project ID

        Returns:
            Project details
        """
        params = {"id": project_id}
        return await self._request("/project", params=params)

    async def get_worker_projects(
        self,
        categories: str = "",
        attributes: str = "",
        price_from: int = 0,
        price_to: int = 0,
        hiring_from: int = 0,
        offers: str = "",
        query: str = "",
        page: int = 1,
    ) -> Dict[str, Any]:
        """Get worker projects"""
        params = {
            "categories": categories,
            "attributes": attributes,
            "price_from": price_from,
            "price_to": price_to,
            "hiring_from": hiring_from,
            "offers": offers,
            "query": query,
            "page": page,
        }
        return await self._request("/projects", params=params)

    async def restart_want(self, want_id: int) -> Dict[str, Any]:
        """Restart want"""
        params = {"id": want_id}
        return await self._request("/restartWant", params=params)

    async def set_favorite(self, categories: str = "", attributes: str = "") -> Dict[str, Any]:
        """Set favorite"""
        params = {"categories": categories, "attributes": attributes}
        return await self._request("/setFavorite", params=params)

    async def stop_want(self, want_id: int) -> Dict[str, Any]:
        """Stop want"""
        params = {"id": want_id}
        return await self._request("/stopWant", params=params)

    async def get_wants_status_list(self) -> Dict[str, Any]:
        """Get wants status list"""
        return await self._request("/wantsStatusList", params={})

    async def get_connects(self) -> Dict[str, Any]:
        """Get connects info (active_connects, all_connects, update_time)

        Returns:
            Dict with keys: active_connects, all_connects, update_time
            Example: {'active_connects': 24, 'all_connects': 30, 'update_time': 1234567890}
        """
        response = await self._request("/projects", params={"page": 1})
        connects = response.get("connects", {})
        return {
            "active_connects": connects.get("active_connects", 0),
            "all_connects": connects.get("all_connects", 0),
            "update_time": connects.get("update_time", 0),
        }
