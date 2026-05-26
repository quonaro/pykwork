"""
ReviewService methods
Review and answer management
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class ReviewService:
    """ReviewService mixin for KworkClient"""

    async def create_answer(self, review_id: int, text: str) -> Dict[str, Any]:
        """Create answer to review"""
        params = {"review_id": review_id, "text": text}
        return await self._request("/createAnswer", params=params)

    async def edit_answer(self, answer_id: int, text: str) -> Dict[str, Any]:
        """Edit answer to review"""
        params = {"answer_id": answer_id, "text": text}
        return await self._request("/editAnswer", params=params)
