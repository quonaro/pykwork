"""
TrackService methods
Track/message management
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class TrackService:
    """TrackService mixin for KworkClient"""

    async def get_tracks(
        self,
        order_id: int = 0,
        track_id: int = 0,
        limit: int = 0,
        direction: str = "",
    ) -> Dict[str, Any]:
        """Get tracks"""
        params = {
            "orderId": order_id,
            "trackId": track_id,
            "limit": limit,
            "direction": direction,
        }
        return await self._request("/getTracks", params=params)

    async def get_voice_message_transcription(self, conversation_id: int) -> Dict[str, Any]:
        """Get voice transcription"""
        params = {"conversation_id": conversation_id}
        return await self._request("/getVoiceMessageTranscription", params=params)

    async def search_order_tracks(self, text: str, order_id: int, page: int = 1) -> Dict[str, Any]:
        """Search order tracks"""
        params = {"text": text, "orderId": order_id, "page": page}
        return await self._request("/searchOrderTracks", params=params)

    async def create_track(
        self,
        user_id: int,
        message_key: str,
        text: str,
        order_id: int = 0,
        uploaded_files: list = None,
        reply_message_id: int = 0,
        with_tracks: int = 0,
    ) -> Dict[str, Any]:
        """Create track"""
        params = {
            "user_id": user_id,
            "message_key": message_key,
            "text": text,
            "order_id": order_id,
            "uploaded_files[]": uploaded_files or [],
            "reply_message_id": reply_message_id,
            "withTracks": with_tracks,
        }
        return await self._request("/inboxCreate", params=params)

    async def delete_track(self, track_id: int) -> Dict[str, Any]:
        """Delete track"""
        params = {"id": track_id}
        return await self._request("/trackDelete", params=params)

    async def edit_track(
        self,
        track_id: int,
        text: str,
        quote_id: int = 0,
        uploaded_files: list = None,
    ) -> Dict[str, Any]:
        """Edit track"""
        params = {
            "id": track_id,
            "text": text,
            "quoteId": quote_id,
            "uploadedFiles[]": uploaded_files or [],
        }
        return await self._request("/trackEdit", params=params)
