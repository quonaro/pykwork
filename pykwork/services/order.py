"""
OrderService methods
Order management endpoints
"""

from typing import Any, Dict, List, Optional

from ..logger import get_logger

logger = get_logger(__name__)


class OrderService:
    """OrderService mixin for KworkClient"""

    async def get_order(self, order_id: int) -> Dict[str, Any]:
        """Get order by ID"""
        params = {"id": order_id}
        return await self._request("/order", params=params)

    async def get_order_files(self, order_id: int) -> Dict[str, Any]:
        """Get order files"""
        params = {"id": order_id}
        return await self._request("/getOrderFiles", params=params)

    async def get_order_header(
        self,
        order_id: int,
        order_hash: Optional[int] = None,
        kwork_hash: Optional[int] = None,
        payer_hash: Optional[int] = None,
        worker_hash: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get order header"""
        params = {"orderId": order_id}
        if order_hash is not None:
            params["orderHash"] = order_hash
        if kwork_hash is not None:
            params["kworkHash"] = kwork_hash
        if payer_hash is not None:
            params["payerHash"] = payer_hash
        if worker_hash is not None:
            params["workerHash"] = worker_hash
        return await self._request("/getOrderHeader", params=params)

    async def get_order_details(self, order_id: int) -> Dict[str, Any]:
        """Get order details"""
        params = {"orderId": order_id}
        return await self._request("/getOrderDetails", params=params)

    async def send_order_for_approval(
        self,
        order_id: int,
        metrics: Optional[List[int]] = None,
        stage_ids: Optional[List[int]] = None,
        files_ids: Optional[List[int]] = None,
    ) -> Dict[str, Any]:
        """Send order for approval"""
        params = {"orderId": order_id}
        if metrics is not None:
            params["metrics[]"] = metrics
        if stage_ids is not None:
            params["stageIds[]"] = stage_ids
        if files_ids is not None:
            params["filesIds[]"] = files_ids
        return await self._request("/sendOrderForApproval", params=params)

    async def approve_order(self, order_id: int, portfolio: int) -> Dict[str, Any]:
        """Approve order"""
        params = {"orderId": order_id, "portfolio": portfolio}
        return await self._request("/approveOrder", params=params)

    async def approve_order_stage(
        self, order_id: int, stage_ids: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """Approve order stage"""
        params = {"orderId": order_id}
        if stage_ids is not None:
            params["stageIds[]"] = stage_ids
        return await self._request("/approveOrderStage", params=params)

    async def send_order_for_revision(
        self,
        order_id: int,
        revision: Optional[str] = None,
        files: Optional[List[int]] = None,
        stage_ids: Optional[List[int]] = None,
    ) -> Dict[str, Any]:
        """Send order for revision"""
        params = {"orderId": order_id}
        if revision is not None:
            params["revision"] = revision
        if files is not None:
            params["files[]"] = files
        if stage_ids is not None:
            params["stageIds[]"] = stage_ids
        return await self._request("/sendOrderForRevision", params=params)

    async def send_bonus(
        self, order_id: int, bonus: int, comment: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send bonus to worker"""
        params = {"orderId": order_id, "bonus": bonus}
        if comment is not None:
            params["comment"] = comment
        return await self._request("/sendBonus", params=params)

    async def send_order_for_arbitration(
        self,
        order_id: int,
        reason_id: int,
        comments: str,
        files: Optional[List[int]] = None,
        stage_ids: Optional[List[int]] = None,
    ) -> Dict[str, Any]:
        """Send order for arbitration"""
        params = {"orderId": order_id, "reasonId": reason_id, "comments": comments}
        if files is not None:
            params["files[]"] = files
        if stage_ids is not None:
            params["stageIds[]"] = stage_ids
        return await self._request("/sendOrderForArbitration", params=params)

    async def get_arbitration_reasons(self, order_id: int) -> Dict[str, Any]:
        """Get arbitration reasons"""
        params = {"orderId": order_id}
        return await self._request("/getArbitrationReasons", params=params)

    async def rate_arbitration(self, id: int, rating: int) -> Dict[str, Any]:
        """Rate arbitration"""
        params = {"id": id, "rating": rating}
        return await self._request("/rateArbitration", params=params)

    async def cancel_order_awaiting_payment(self, order_id: int) -> Dict[str, Any]:
        """Cancel order awaiting payment"""
        params = {"order_id": order_id}
        return await self._request("/cancelOrderAwaitingPayment", params=params)

    async def pay_order_awaiting_payment(self, order_id: int) -> Dict[str, Any]:
        """Pay order awaiting payment"""
        params = {"order_id": order_id}
        return await self._request("/payOrderAwaitingPayment", params=params)

    async def allow_order_portfolio_upload(self, order_id: int) -> Dict[str, Any]:
        """Allow order portfolio upload"""
        params = {"order_id": order_id}
        return await self._request("/allowOrderPortfolioUpload", params=params)

    async def get_order_provided_data(self, order_id: int) -> Dict[str, Any]:
        """Get order provided data"""
        params = {"order_id": order_id}
        return await self._request("/getOrderProvidedData", params=params)

    async def set_order_rating(
        self, order_id: int, speed: int, quality: int, communication: int
    ) -> Dict[str, Any]:
        """Set order rating"""
        params = {
            "order_id": order_id,
            "speed": speed,
            "quality": quality,
            "communication": communication,
        }
        return await self._request("/setOrderRating", params=params)

    async def send_order_receipt_link_for_verification(
        self, receipt_id: int, receipt_link: str
    ) -> Dict[str, Any]:
        """Send order receipt link for verification"""
        params = {"receiptId": receipt_id, "receiptLink": receipt_link}
        return await self._request("/sendOrderReceiptLinkForVerification", params=params)

    async def save_order_note(self, order_id: int, note: str) -> Dict[str, Any]:
        """Save order note"""
        params = {"order_id": order_id}
        # Note: This endpoint uses application/x-www-form-urlencoded body
        # Implementation may need special handling
        return await self._request("/saveOrderNote", params=params)

    async def delete_order_note(self, order_id: int) -> Dict[str, Any]:
        """Delete order note"""
        params = {"order_id": order_id}
        return await self._request("/deleteOrderNote", params=params)

    async def send_order_requirements(
        self,
        order_id: int,
        requirements: Optional[str] = None,
        files: Optional[List[int]] = None,
        metrics: Optional[List[int]] = None,
    ) -> Dict[str, Any]:
        """Send order requirements"""
        params = {"orderId": order_id}
        if requirements is not None:
            params["requirements"] = requirements
        if files is not None:
            params["files[]"] = files
        if metrics is not None:
            params["metrics[]"] = metrics
        return await self._request("/sendOrderRequirements", params=params)

    async def offer_order_options(
        self,
        order_id: int,
        options: Optional[Dict[str, int]] = None,
        custom_options: Optional[Dict[str, int]] = None,
        updated_package: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Offer order options"""
        params = {"orderId": order_id}
        if options is not None:
            params["options"] = options
        if custom_options is not None:
            params["customOptions"] = custom_options
        if updated_package is not None:
            params["updatedPackage"] = updated_package
        return await self._request("/offerOrderOptions", params=params)

    async def get_extras_available_for_order(self, order_id: int) -> Dict[str, Any]:
        """Get extras available for order"""
        params = {"orderId": order_id}
        return await self._request("/getExtrasAvailableForOrder", params=params)

    async def get_ordered_extras(self, order_id: int) -> Dict[str, Any]:
        """Get ordered extras"""
        params = {"orderId": order_id}
        return await self._request("/getOrderedExtras", params=params)

    async def get_custom_options_presets(self, order_id: int) -> Dict[str, Any]:
        """Get custom options presets"""
        params = {"order_id": order_id}
        return await self._request("/getCustomOptionsPresets", params=params)

    async def get_order_cancellation_reasons(self, order_id: int) -> Dict[str, Any]:
        """Get order cancellation reasons"""
        params = {"orderId": order_id}
        return await self._request("/getOrderCancellationReasons", params=params)

    async def order_kwork(
        self,
        kwork_id: int,
        kworks_count: Optional[int] = None,
        volume_type_id: Optional[int] = None,
        volume: Optional[float] = None,
        package_id: Optional[int] = None,
        extras: Optional[Dict[str, int]] = None,
        channel_format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Order kwork"""
        params = {"kworkId": kwork_id}
        if kworks_count is not None:
            params["kworksCount"] = kworks_count
        if volume_type_id is not None:
            params["volumeTypeId"] = volume_type_id
        if volume is not None:
            params["volume"] = volume
        if package_id is not None:
            params["packageId"] = package_id
        if extras is not None:
            params["extras"] = extras
        if channel_format is not None:
            params["channel_format"] = channel_format
        return await self._request("/orderKwork", params=params)

    async def repeat_order(self, order_id: int) -> Dict[str, Any]:
        """Repeat order"""
        params = {"orderId": order_id}
        return await self._request("/repeatOrder", params=params)
