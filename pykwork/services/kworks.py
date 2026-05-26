"""
KworksService methods
User kwork management
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class KworksService:
    """KworksService mixin for KworkClient"""

    async def delete_kwork(self, kwork_id: int) -> Dict[str, Any]:
        """Delete kwork"""
        params = {"kwork_id": kwork_id}
        return await self._request("/deleteKwork", params=params)

    async def get_kworks_status_list(self) -> Dict[str, Any]:
        """Get kwork status list"""
        return await self._request("/kworksStatusList", params={})

    async def mark_kwork_as_favorite(self, kwork_id: int, is_favorite: bool) -> Dict[str, Any]:
        """Mark kwork as favorite"""
        params = {"kwork_id": kwork_id, "is_favorite": is_favorite}
        return await self._request("/markKworkAsFavorite", params=params)

    async def mark_kwork_as_hidden(self, kwork_id: int, is_hidden: bool) -> Dict[str, Any]:
        """Mark kwork as hidden"""
        params = {"kwork_id": kwork_id, "is_hidden": is_hidden}
        return await self._request("/markKworkAsHidden", params=params)

    async def mark_kworks_black_friday(self, kwork_id: int) -> Dict[str, Any]:
        """Mark for Black Friday"""
        params = {"kworkId": kwork_id}
        return await self._request("/markKworksBlackFriday", params=params)

    async def pause_kwork(self, kwork_id: int) -> Dict[str, Any]:
        """Pause kwork"""
        params = {"kwork_id": kwork_id}
        return await self._request("/pauseKwork", params=params)

    async def set_available_at_weekends(self, is_available: bool) -> Dict[str, Any]:
        """Set weekend availability"""
        params = {"is_available": is_available}
        return await self._request("/setAvailableAtWeekends", params=params)

    async def start_kwork(self, kwork_id: int) -> Dict[str, Any]:
        """Start kwork"""
        params = {"kwork_id": kwork_id}
        return await self._request("/startKwork", params=params)
