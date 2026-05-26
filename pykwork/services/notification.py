"""
NotificationService methods
Notification endpoints
"""

from typing import Any, Dict, List, Optional

from ..logger import get_logger

logger = get_logger(__name__)


class NotificationService:
    """NotificationService mixin for KworkClient"""

    async def get_notifications(self) -> Dict[str, Any]:
        """Get notifications"""
        return await self._request("/notifications", params={})

    async def notifications_received(self, ids: List[int]) -> Dict[str, Any]:
        """Mark notifications as received"""
        params = {"ids[]": ids}
        return await self._request("/notificationsReceived", params=params)

    async def notifications_fetch(self, page: int = 1, uad: Optional[str] = None) -> Dict[str, Any]:
        """Fetch unread push events"""
        params = {"page": page}
        if uad is not None:
            params["uad"] = uad
        return await self._request("/notificationsFetch", params=params)

    async def validate_event(self, id: int) -> Dict[str, Any]:
        """Validate push event"""
        params = {"id": id}
        return await self._request("/validateEvent", params=params)

    async def get_in_app_notification(
        self,
        uad: str,
        os_type: str,
        os_version: str,
        app_version: str,
        last_notification_type: Optional[str] = None,
        last_notification_id: Optional[int] = None,
        last_notification_action_timestamp: Optional[int] = None,
        last_notification_action_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get in-app notification"""
        params = {
            "uad": uad,
            "os_type": os_type,
            "os_version": os_version,
            "app_version": app_version,
        }
        if last_notification_type is not None:
            params["lastNotificationType"] = last_notification_type
        if last_notification_id is not None:
            params["lastNotificationId"] = last_notification_id
        if last_notification_action_timestamp is not None:
            params["lastNotificationActionTimestamp"] = last_notification_action_timestamp
        if last_notification_action_id is not None:
            params["lastNotificationActionId"] = last_notification_action_id
        return await self._request("/getInAppNotification", params=params)

    async def push_in_app_notification_log(
        self,
        notification_id: int,
        action: int,
        previous_show_date: Optional[int] = None,
        uad: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Log in-app notification"""
        params = {"notificationId": notification_id, "action": action}
        if previous_show_date is not None:
            params["previousShowDate"] = previous_show_date
        if uad is not None:
            params["uad"] = uad
        return await self._request("/pushInAppNotificationLog", params=params)
