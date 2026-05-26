"""
FileService methods
File upload and management
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class FileService:
    """FileService mixin for KworkClient"""

    async def file_upload(self, file_data: bytes) -> Dict[str, Any]:
        """Upload file"""
        # Note: This endpoint requires multipart/form-data
        # Implementation may need special handling for file uploads
        params = {}
        return await self._request("/fileUpload", params=params)

    async def voice_upload(self, file_data: bytes) -> Dict[str, Any]:
        """Upload voice file"""
        # Note: This endpoint requires multipart/form-data
        # Implementation may need special handling for file uploads
        params = {}
        return await self._request("/voiceUpload", params=params)

    async def file_delete(self, file_id: int) -> Dict[str, Any]:
        """Delete file"""
        params = {"id": file_id}
        return await self._request("/fileDelete", params=params)

    async def uploaded_file(self, path: str) -> Dict[str, Any]:
        """Get uploaded file info"""
        params = {"path": path}
        return await self._request("/uploadedFile", params=params)

    async def miniature(self, path: str) -> Dict[str, Any]:
        """Get file miniature"""
        params = {"path": path}
        return await self._request("/miniature", params=params)
