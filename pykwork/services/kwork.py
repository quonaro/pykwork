"""
KworkDetailsService methods
Kwork details endpoints
"""

from typing import Any, Dict

from ..logger import get_logger

logger = get_logger(__name__)


class KworkDetailsService:
    """KworkDetailsService mixin for KworkClient"""

    async def create_kwork_complain(
        self, kwork_id: int, category_id: int, text: str
    ) -> Dict[str, Any]:
        """Create kwork complaint"""
        params = {"kwork_id": kwork_id, "category_id": category_id, "text": text}
        return await self._request("/createKworkComplain", params=params)

    async def get_complain_categories(self) -> Dict[str, Any]:
        """Get complaint categories"""
        return await self._request("/getComplainCategories", params={})

    async def get_kwork_answers(self, kwork_id: int) -> Dict[str, Any]:
        """Get FAQ"""
        params = {"kwork_id": kwork_id}
        return await self._request("/getKworkAnswers", params=params)

    async def get_kwork_details(self, kwork_id: int) -> Dict[str, Any]:
        """Get kwork details"""
        params = {"kwork_id": kwork_id}
        return await self._request("/getKworkDetails", params=params)

    async def get_kwork_details_extra(self, kwork_id: int) -> Dict[str, Any]:
        """Get extra kwork details"""
        params = {"kwork_id": kwork_id}
        return await self._request("/getKworkDetailsExtra", params=params)

    async def get_kwork_links_table(self, kwork_id: int) -> Dict[str, Any]:
        """Get kwork links table"""
        params = {"kwork_id": kwork_id}
        return await self._request("/getKworkLinksTable", params=params)

    async def get_kwork_portfolios(self, kwork_id: int) -> Dict[str, Any]:
        """Get kwork portfolios"""
        params = {"kwork_id": kwork_id}
        return await self._request("/getKworkPortfolios", params=params)

    async def get_kwork_reviews(self, kwork_id: int) -> Dict[str, Any]:
        """Get kwork reviews"""
        params = {"kwork_id": kwork_id}
        return await self._request("/getKworkReviews", params=params)

    async def order_kwork(self, kwork_id: int, **kwargs) -> Dict[str, Any]:
        """Order kwork"""
        params = {"kwork_id": kwork_id, **kwargs}
        return await self._request("/orderKwork", params=params)

    async def recharge_balance(
        self,
        order_id: int,
        payment_id: int,
        amount: int,
        payment_type: str,
        country_group_code: str,
    ) -> Dict[str, Any]:
        """Recharge balance"""
        params = {
            "orderId": order_id,
            "paymentId": payment_id,
            "amount": amount,
            "paymentType": payment_type,
            "countryGroupCode": country_group_code,
        }
        return await self._request("/rechargeBalance", params=params)
