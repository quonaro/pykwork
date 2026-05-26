"""
PaymentService methods
Payment and billing endpoints
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class PaymentService:
    """PaymentService mixin for KworkClient"""

    async def get_payment_methods(self) -> Dict[str, Any]:
        """Get available payment methods"""
        return await self._request("/getPaymentMethods", params={})

    async def get_bill_refill_url(self, amount: int, payment_type: str) -> Dict[str, Any]:
        """Get bill refill URL"""
        params = {"amount": amount, "paymentType": payment_type}
        return await self._request("/getBillRefillUrl", params=params)
