"""
DialogService methods
Dialog and message management
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class DialogService:
    """DialogService mixin for KworkClient"""

    async def hide_dialog(self, user_id: int, is_restore: int = 0) -> Dict[str, Any]:
        """Hide/restore dialog"""
        params = {"userId": user_id, "isRestore": is_restore}
        return await self._request("/hideDialog", params=params)

    async def get_dialogs(self, page: int = 1, filter_str: str = "") -> Dict[str, Any]:
        """Get dialog list"""
        params = {"page": page, "filter": filter_str}
        return await self._request("/dialogs", params=params)

    async def get_dialog(self, dialog_id: int, with_tracks: int = 0) -> Dict[str, Any]:
        """Get specific dialog"""
        params = {"id": dialog_id, "withTracks": with_tracks}
        return await self._request("/getDialog", params=params)

    async def get_quiz_questions(self) -> Dict[str, Any]:
        """Get quiz questions"""
        return await self._request("/getFishingTutorialQuestions", params={})

    async def mark_dialog_read(self, user_id: int) -> Dict[str, Any]:
        """Mark dialog as read"""
        params = {"user_id": user_id}
        return await self._request("/inboxRead", params=params)

    async def set_quiz_status(self, status: int) -> Dict[str, Any]:
        """Set quiz status"""
        params = {"status": status}
        return await self._request("/setFishingTutorialStatus", params=params)

    async def set_dialog_starred(self, user_id: int, is_starred: int) -> Dict[str, Any]:
        """Mark dialog as starred"""
        params = {"userId": user_id, "isStarred": is_starred}
        return await self._request("/setDialogStarred", params=params)

    async def mark_dialog_unread(self, user_id: int) -> Dict[str, Any]:
        """Mark dialog as unread"""
        params = {"user_id": user_id}
        return await self._request("/unreadDialog", params=params)

    async def archive_dialog(self, user_id: int) -> Dict[str, Any]:
        """Archive dialog"""
        params = {"userId": user_id}
        return await self._request("/archiveDialog", params=params)

    async def unarchive_dialog(self, user_id: int) -> Dict[str, Any]:
        """Unarchive dialog"""
        params = {"userId": user_id}
        return await self._request("/unarchiveDialog", params=params)

    async def search_dialogs(self, query: str, page: int = 1) -> Dict[str, Any]:
        """Search dialogs"""
        params = {"query": query, "page": page}
        return await self._request("/searchDialogs", params=params)

    async def is_dialog_allow(self, user_id: int) -> Dict[str, Any]:
        """Check if dialog is allowed"""
        params = {"userId": user_id}
        return await self._request("/isDialogAllow", params=params)

    async def blocked_dialog_list(self) -> Dict[str, Any]:
        """Get blocked dialog list"""
        return await self._request("/blockedDialogList", params={})

    async def blocked_dialogs(self) -> Dict[str, Any]:
        """Get blocked dialogs"""
        return await self._request("/blockedDialogs", params={})

    async def allow_inbox_request(self, inbox_id: int, is_accept: int) -> Dict[str, Any]:
        """Allow/deny inbox request"""
        params = {"inboxId": inbox_id, "isAccept": is_accept}
        return await self._request("/allowInboxRequest", params=params)

    async def inbox_custom_request_decline(self, message_id: int) -> Dict[str, Any]:
        """Decline custom request"""
        params = {"message_id": message_id}
        return await self._request("/inboxCustomRequestDecline", params=params)

    async def inbox_payer_decline(self, message_id: int) -> Dict[str, Any]:
        """Decline kwork offer by payer"""
        params = {"message_id": message_id}
        return await self._request("/inboxPayerDecline", params=params)

    async def inbox_worker_decline(self, message_id: int) -> Dict[str, Any]:
        """Decline kwork offer by worker"""
        params = {"message_id": message_id}
        return await self._request("/inboxWorkerDecline", params=params)

    async def typing(self, recipient_id: int, order_id: int = None) -> Dict[str, Any]:
        """Send typing indicator"""
        params = {"recipientId": recipient_id}
        if order_id is not None:
            params["orderId"] = order_id
        return await self._request("/typing", params=params)
