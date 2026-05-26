"""
CatalogService methods
Catalog-related endpoints
"""

from typing import Any, Dict, Optional

from ..logger import get_logger

logger = get_logger(__name__)


class CatalogService:
    """CatalogService mixin for KworkClient"""

    async def get_catalog_filters(
        self,
        category_id: Optional[int] = None,
        classifier_id: Optional[int] = None,
        is_search: int = 0,
        query: Optional[str] = None,
        unembedded: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Get catalog filters"""
        params = {}
        if category_id is not None:
            params["categoryId"] = category_id
        if classifier_id is not None:
            params["classifierId"] = classifier_id
        if is_search is not None:
            params["isSearch"] = is_search
        if query is not None:
            params["query"] = query
        if unembedded is not None:
            params["unembedded"] = unembedded
        if filters is not None:
            params.update(filters)
        return await self._request("/catalogFilters", params=params)

    async def get_main_data(self) -> Dict[str, Any]:
        """Get main data (v1)"""
        return await self._request("/mainData", params={})

    async def get_main_data_v2(self) -> Dict[str, Any]:
        """Get main data (v2)"""
        return await self._request("/mainDataV2", params={})

    async def catalog_main(self) -> Dict[str, Any]:
        """Get catalog main data"""
        return await self._request("/catalogMain", params={})

    async def catalog_main_v2(self) -> Dict[str, Any]:
        """Get catalog main data v2"""
        return await self._request("/catalogMainv2", params={})

    async def get_rubrics(self) -> Dict[str, Any]:
        """Get rubrics"""
        return await self._request("/rubrics", params={})

    async def catalog_rubrics(self) -> Dict[str, Any]:
        """Get catalog rubrics"""
        return await self._request("/catalogRubrics", params={})

    async def catalog_categories(self, rubric_id: int) -> Dict[str, Any]:
        """Get catalog categories"""
        params = {"rubricId": rubric_id}
        return await self._request("/catalogCategories", params=params)

    async def translation_languages(self) -> Dict[str, Any]:
        """Get translation languages"""
        return await self._request("/translationLanguages", params={})

    async def category_attributes(self, category_id: int) -> Dict[str, Any]:
        """Get category attributes"""
        params = {"categoryId": category_id}
        return await self._request("/categoryAttributes", params=params)

    async def positive_reviews_count(self, category_id: int) -> Dict[str, Any]:
        """Get positive reviews count"""
        params = {"categoryId": category_id}
        return await self._request("/positiveReviewsCount", params=params)

    async def cities(self) -> Dict[str, Any]:
        """Get cities"""
        return await self._request("/cities", params={})

    async def countries(self) -> Dict[str, Any]:
        """Get countries"""
        return await self._request("/countries", params={})

    async def payer_company_modal_url(self) -> Dict[str, Any]:
        """Get payer company modal URL"""
        return await self._request("/getPayerCompanyModalUrl", params={})

    async def get_favorite_kworks(self) -> Dict[str, Any]:
        """Get favorite kworks"""
        return await self._request("/favoriteKworks", params={})

    async def get_hidden_kworks(self) -> Dict[str, Any]:
        """Get hidden kworks"""
        return await self._request("/hiddenKworks", params={})

    async def get_general_kworks(self) -> Dict[str, Any]:
        """Get general kworks"""
        return await self._request("/generalKworks", params={})

    async def get_viewed_kworks(self) -> Dict[str, Any]:
        """Get viewed kworks"""
        return await self._request("/viewedKworks", params={})

    async def search_kworks(self, query: str) -> Dict[str, Any]:
        """Search kworks by query"""
        params = {"query": query}
        return await self._request("/searchKworks", params=params)

    async def search_kworks_for_user(self, query: str) -> Dict[str, Any]:
        """Search kworks for user"""
        params = {"query": query}
        return await self._request("/searchKworksForUser", params=params)
