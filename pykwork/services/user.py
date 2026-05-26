"""
UserService methods
User account management endpoints
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class UserService:
    """UserService mixin for KworkClient"""

    async def get_user_by_username(self, username: str) -> Dict[str, Any]:
        """Get user by username"""
        params = {"username": username}
        return await self._request("/userByUsername", params=params)

    async def get_user_kworks(self, user_id: int, page: int = 1) -> Dict[str, Any]:
        """Get user kworks"""
        params = {"user_id": user_id, "page": page}
        return await self._request("/userKworks", params=params)

    async def get_user_categories(self, user_id: int) -> Dict[str, Any]:
        """Get user categories"""
        params = {"user_id": user_id}
        return await self._request("/kworksCategoriesList", params=params)

    async def get_user_reviews(
        self, user_id: int, page: int = 1, review_type: str = ""
    ) -> Dict[str, Any]:
        """Get user reviews"""
        params = {"user_id": user_id, "page": page, "type": review_type}
        return await self._request("/userReviews", params=params)

    async def block_dialog(self, block_user_id: int) -> Dict[str, Any]:
        """Block dialog with user"""
        params = {"blockUserId": block_user_id}
        return await self._request("/blockDialog", params=params)

    async def unblock_dialog(self, block_user_id: int) -> Dict[str, Any]:
        """Unblock dialog with user"""
        params = {"blockUserId": block_user_id}
        return await self._request("/unblockDialog", params=params)

    async def get_users_last_order_info(self, interlocutor_id: int) -> Dict[str, Any]:
        """Get last order info with interlocutor"""
        params = {"interlocutorId": interlocutor_id}
        return await self._request("/getUsersLastOrderInfo", params=params)

    async def orders_between(self, user_id: int) -> Dict[str, Any]:
        """Get active orders between users"""
        params = {"user_id": user_id}
        return await self._request("/ordersBetween", params=params)
