"""
StageService methods
Order stage management
"""

from typing import Any, Dict, List, Optional

from ..logger import get_logger

logger = get_logger(__name__)


class StageService:
    """StageService mixin for KworkClient"""

    async def create_stage(
        self, order_id: int, extend_time: int, stages: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Create stage in order"""
        params = {"order_id": order_id, "extend_time": extend_time, "stages": stages}
        return await self._request("/createStage", params=params)

    async def add_stage(
        self, order_id: int, extend_time: int, stages: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Add stage to order"""
        params = {"order_id": order_id, "extend_time": extend_time, "stages": stages}
        return await self._request("/addStage", params=params)

    async def order_stage(self, order_id: int, stage_id: int) -> Dict[str, Any]:
        """Reserve stage"""
        params = {"order_id": order_id, "stage_id": stage_id}
        return await self._request("/orderStage", params=params)

    async def edit_stage(
        self, order_id: int, extend_time: int, stages: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Edit stage in order"""
        params = {"orderId": order_id, "extendTime": extend_time, "stages": stages}
        return await self._request("/editStage", params=params)

    async def update_stage_progress(
        self,
        order_id: int,
        stages: Dict[str, Any],
        comment: str,
        metrics: Optional[List[int]] = None,
        track_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Update stage progress"""
        params = {"order_id": order_id, "stages": stages, "comment": comment}
        if metrics is not None:
            params["metrics[]"] = metrics
        if track_id is not None:
            params["trackId"] = track_id
        return await self._request("/updateStageProgress", params=params)
