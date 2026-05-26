"""
InboxService methods
Inbox management
"""

from typing import Any, Dict, List, Optional

from ..logger import get_logger

logger = get_logger(__name__)


class InboxService:
    """InboxService mixin for KworkClient"""

    async def get_inbox_tracks(
        self,
        username: Optional[str] = None,
        page: Optional[int] = None,
        last_conversation_id: Optional[int] = None,
        direction: Optional[str] = None,
        limit: Optional[int] = None,
        user_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get inbox tracks"""
        params = {}
        if username is not None:
            params["username"] = username
        if page is not None:
            params["page"] = page
        if last_conversation_id is not None:
            params["lastConversationId"] = last_conversation_id
        if direction is not None:
            params["direction"] = direction
        if limit is not None:
            params["limit"] = limit
        if user_id is not None:
            params["userId"] = user_id
        return await self._request("/getInboxTracks", params=params)

    async def inboxes(self, username: str, page: Optional[str] = None) -> Dict[str, Any]:
        """Get inbox messages"""
        params = {"username": username}
        if page is not None:
            params["page"] = page
        return await self._request("/inboxes", params=params)

    async def inbox_track_message(self, conversation_id: int) -> Dict[str, Any]:
        """Get inbox/track message by conversation ID"""
        params = {"conversationId": conversation_id}
        return await self._request("/inboxTrackMessage", params=params)

    async def inbox_complain_message(
        self,
        message_id: int,
        complain_category_id: Optional[int] = None,
        comment: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Complain about message"""
        params = {"message_id": message_id}
        if complain_category_id is not None:
            params["complain_category_id"] = complain_category_id
        if comment is not None:
            params["comment"] = comment
        return await self._request("/inboxComplainMessage", params=params)

    async def inbox_delete(self, id: int, with_tracks: Optional[int] = None) -> Dict[str, Any]:
        """Delete inbox"""
        params = {"id": id}
        if with_tracks is not None:
            params["withTracks"] = with_tracks
        return await self._request("/inboxDelete", params=params)

    async def inbox_edit(
        self,
        id: int,
        text: str,
        uploaded_files: Optional[Dict[str, int]] = None,
        reply_message_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Edit inbox"""
        params = {"id": id, "text": text}
        if uploaded_files is not None:
            params["uploaded_files"] = uploaded_files
        if reply_message_id is not None:
            params["reply_message_id"] = reply_message_id
        return await self._request("/inboxEdit", params=params)

    async def inbox_forward(self, user_id: int, message_ids: List[int]) -> Dict[str, Any]:
        """Forward inbox"""
        params = {"userId": user_id, "message_ids": message_ids}
        return await self._request("/inboxForward", params=params)

    async def inbox_create(
        self,
        user_id: int,
        text: str,
        uuid: Optional[str] = None,
        message_key: Optional[str] = None,
        order_id: Optional[int] = None,
        kwork_id: Optional[int] = None,
        uploaded_files: Optional[List[int]] = None,
        reply_message_id: Optional[int] = None,
        with_tracks: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Create inbox message"""
        params = {"user_id": user_id, "text": text}
        if uuid is not None:
            params["uuid"] = uuid
        if message_key is not None:
            params["message_key"] = message_key
        if order_id is not None:
            params["order_id"] = order_id
        if kwork_id is not None:
            params["kwork_id"] = kwork_id
        if uploaded_files is not None:
            params["uploaded_files[]"] = uploaded_files
        if reply_message_id is not None:
            params["reply_message_id"] = reply_message_id
        if with_tracks is not None:
            params["withTracks"] = with_tracks
        return await self._request("/inboxCreate", params=params)

    async def inbox_message(self, message_id: int) -> Dict[str, Any]:
        """Get inbox message by ID"""
        params = {"messageId": message_id}
        return await self._request("/inboxMessage", params=params)

    async def mark_inbox_tracks_as_read(
        self, user_id: int, conversation_ids: List[int]
    ) -> Dict[str, Any]:
        """Mark inbox tracks as read"""
        params = {"userId": user_id, "conversationIds[]": conversation_ids}
        return await self._request("/markInboxTracksAsRead", params=params)

    async def search_inboxes(
        self, query: str, user_id: Optional[int] = None, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Search inboxes"""
        params = {"query": query}
        if user_id is not None:
            params["userId"] = user_id
        if page is not None:
            params["page"] = page
        return await self._request("/searchInboxes", params=params)

    async def search_messages(
        self, text: str, user_id: int, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Search messages"""
        params = {"text": text, "userId": user_id}
        if page is not None:
            params["page"] = page
        return await self._request("/searchMessages", params=params)

    async def inbox_read(
        self, user_id: int, messages: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """Mark inbox as read"""
        params = {"user_id": user_id}
        if messages is not None:
            params["messages"] = messages
        return await self._request("/inboxRead", params=params)

    async def send_user_status(
        self, user_id: int, status: str, order_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Send user status"""
        params = {"user_id": user_id, "status": status}
        if order_id is not None:
            params["order_id"] = order_id
        return await self._request("/sendUserStatus", params=params)

    async def mark_voice_message_heard(self, conversation_id: int) -> Dict[str, Any]:
        """Mark voice message as heard"""
        params = {"conversation_id": conversation_id}
        return await self._request("/markVoiceMessageHeard", params=params)

    async def update_chat_draft_message(
        self, user_id: int, message: Optional[str] = None, files: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """Update chat draft message"""
        params = {"userId": user_id}
        if message is not None:
            params["message"] = message
        if files is not None:
            params["files[]"] = files
        return await self._request("/updateChatDraftMessage", params=params)
