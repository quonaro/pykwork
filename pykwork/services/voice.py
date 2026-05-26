"""
VoiceService methods
Voice message management
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class VoiceService:
    """VoiceService mixin for KworkClient"""

    async def get_voice_message_transcription(self, conversation_id: int) -> Dict[str, Any]:
        """Get voice message transcription"""
        params = {"conversation_id": conversation_id}
        return await self._request("/getVoiceMessageTranscription", params=params)

    async def get_voice_message_convert_status(self, file_id: int) -> Dict[str, Any]:
        """Get voice message convert status"""
        params = {"file_id": file_id}
        return await self._request("/getVoiceMessageConvertStatus", params=params)

    async def set_voice_message_speed(self, conversation_id: int, speed: float) -> Dict[str, Any]:
        """Set voice message playback speed"""
        params = {"conversation_id": conversation_id, "speed": speed}
        return await self._request("/setVoiceMessageSpeed", params=params)

    async def set_voice_message_receiving(
        self, conversation_id: int, is_receiving: int
    ) -> Dict[str, Any]:
        """Set voice message receiving status"""
        params = {"conversation_id": conversation_id, "isReceiving": is_receiving}
        return await self._request("/setVoiceMessageReceiving", params=params)
