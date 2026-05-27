"""
Kwork API Client (Async)
Main async client for interacting with Kwork API
"""

import base64
from typing import Any, Dict, List, Optional

import httpx

from .exceptions import KworkAuthError, KworkRequestError
from .logger import get_logger
from .services.catalog import CatalogService
from .services.dialog import DialogService
from .services.exchange import ExchangeService
from .services.file import FileService
from .services.inbox import InboxService
from .services.kwork import KworkDetailsService
from .services.kworks import KworksService
from .services.notification import NotificationService
from .services.offer import OfferService
from .services.order import OrderService
from .services.payment import PaymentService
from .services.review import ReviewService
from .services.stage import StageService
from .services.track import TrackService
from .services.user import UserService
from .services.voice import VoiceService

logger = get_logger(__name__)


class KworkClient(
    UserService,
    DialogService,
    ExchangeService,
    CatalogService,
    KworkDetailsService,
    KworksService,
    InboxService,
    TrackService,
    NotificationService,
    FileService,
    OrderService,
    PaymentService,
    ReviewService,
    VoiceService,
    StageService,
    OfferService,
):
    """Main async client for Kwork API"""

    BASE_URL = "https://api.kwork.ru"
    DEFAULT_API_USER = "mobile_api"
    DEFAULT_API_PASS = "qFvfRl7w"

    def __init__(
        self,
        username: str,
        password: str,
        uad: str = "test",
        device: str = "test",
        timeout: int = 10,
        log_level: int = 30,  # WARNING
        http_proxy: str | None = None,
        https_proxy: str | None = None,
    ):
        """
        Initialize Kwork API client

        Args:
            username: Kwork username (email)
            password: Kwork password
            uad: Unique device identifier
            device: Device model
            timeout: Request timeout in seconds
            log_level: Logging level (default: WARNING)
            http_proxy: HTTP proxy URL (e.g., 'http://proxy.example.com:8080')
            https_proxy: HTTPS proxy URL (e.g., 'http://proxy.example.com:8080')
        """
        self.username = username
        self.password = password
        self.uad = uad
        self.device = device
        self.timeout = timeout
        self.http_proxy = http_proxy
        self.https_proxy = https_proxy
        self._token: Optional[str] = None
        self._client: Optional[httpx.AsyncClient] = None

        # Set logger level
        global logger
        logger.setLevel(log_level)

    def _create_auth_header(self, username: str, password: str) -> str:
        """Create Basic Auth header"""
        credentials = f"{username}:{password}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded}"

    def _get_headers(self) -> Dict[str, str]:
        """Get default headers for requests"""
        return {
            "Content-Type": "application/json",
            "User-Agent": "KworkAPILibrary/2.0",
            "Authorization": self._create_auth_header(self.DEFAULT_API_USER, self.DEFAULT_API_PASS),
        }

    async def _request(
        self,
        endpoint: str,
        method: str = "POST",
        params: Optional[Dict[str, Any]] = None,
        require_auth: bool = True,
    ) -> Dict[str, Any]:
        """
        Make a request to Kwork API

        Args:
            endpoint: API endpoint (e.g., '/signIn')
            method: HTTP method (default: POST)
            params: Query parameters
            require_auth: Whether authentication token is required

        Returns:
            Response data as dictionary

        Raises:
            KworkAuthError: If authentication fails
            KworkRequestError: If request fails
        """
        if require_auth and not self._token:
            raise KworkAuthError("Not authenticated. Call login() first.")

        if not self._client:
            raise KworkAuthError("Client not initialized. Use async context manager.")

        url = f"{self.BASE_URL}{endpoint}"
        headers = self._get_headers()

        # Add common parameters
        if params is None:
            params = {}

        if require_auth:
            params["token"] = self._token

        params["uad"] = self.uad
        params["device"] = self.device
        params["slrememberme"] = "test"

        try:
            if method == "POST":
                response = await self._client.post(
                    url, headers=headers, params=params, timeout=self.timeout
                )
            else:
                response = await self._client.get(
                    url, headers=headers, params=params, timeout=self.timeout
                )

            data = response.json()

            if not data.get("success"):
                error_message = data.get("error", "Unknown error")
                logger.error(f"API error: {error_message}")
                raise KworkRequestError(
                    f"API error: {error_message}",
                    status_code=response.status_code,
                    response=data,
                )

            return data

        except httpx.HTTPError as e:
            logger.error(f"HTTP error: {str(e)}")
            raise KworkRequestError(f"HTTP error: {str(e)}")

    async def login(self) -> Dict[str, Any]:
        """
        Authenticate with Kwork API

        Returns:
            Authentication response with token

        Raises:
            KworkAuthError: If authentication fails
        """
        params = {
            "login": self.username,
            "password": self.password,
            "uad": self.uad,
            "device": self.device,
        }

        try:
            url = f"{self.BASE_URL}/signIn"
            headers = self._get_headers()
            response = await self._client.post(
                url, headers=headers, params=params, timeout=self.timeout
            )
            data = response.json()

            if not data.get("success"):
                error_message = data.get("error", "Authentication failed")
                logger.error(f"Authentication failed: {error_message}")
                raise KworkAuthError(error_message)

            self._token = data["response"]["token"]
            logger.info("Authentication successful")
            return data

        except httpx.HTTPError as e:
            logger.error(f"Authentication request failed: {str(e)}")
            raise KworkAuthError(f"Authentication request failed: {str(e)}")

    async def get_actor(self, make_online: int = 0) -> Dict[str, Any]:
        """
        Get current user information

        Args:
            make_online: Set online status (0 or 1)

        Returns:
            User information
        """
        params = {"makeOnline": make_online}
        return await self._request("/actor", params=params)

    async def get_user(self, user_id: int, make_online: int = 0) -> Dict[str, Any]:
        """
        Get user information by ID

        Args:
            user_id: User ID
            make_online: Set online status (0 or 1)

        Returns:
            User information
        """
        params = {"id": user_id, "makeOnline": make_online}
        return await self._request("/user", params=params)

    async def get_projects(
        self,
        page: int = 1,
        categories: Optional[str] = None,
        price_to: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get projects (connects) from Kwork

        Args:
            page: Page number
            categories: Category ID for filtering
            price_to: Maximum price for filtering

        Returns:
            List of projects
        """
        params = {"page": page}

        if categories:
            params["categories"] = categories
        if price_to:
            params["price_to"] = price_to

        response = await self._request("/projects", params=params)
        return response.get("response", [])

    async def get_connects(self) -> Dict[str, Any]:
        """Get connects info (active_connects, all_connects, update_time)

        Returns:
            Dict with keys: active_connects, all_connects, update_time
            Example: {'active_connects': 24, 'all_connects': 30, 'update_time': 1234567890}
        """
        response = await self._request("/projects", params={"page": 1})
        connects = response.get("connects", {})
        return {
            "active_connects": connects.get("active_connects", 0),
            "all_connects": connects.get("all_connects", 0),
            "update_time": connects.get("update_time", 0),
        }

    async def get_categories(self, category_type: int = 1) -> List[Dict[str, Any]]:
        """
        Get categories for filtering projects

        Args:
            category_type: Category type (1 for exchange categories)

        Returns:
            List of categories
        """
        params = {"type": category_type}
        response = await self._request("/categories", params=params)
        return response.get("response", [])

    async def get_offers(self, page: int = 1) -> List[Dict[str, Any]]:
        """
        Get user's offers

        Args:
            page: Page number

        Returns:
            List of offers
        """
        params = {"page": page}
        response = await self._request("/offers", params=params)
        return response.get("response", [])

    async def get_all_offers(self) -> List[Dict[str, Any]]:
        """
        Get all user's offers (paginated)

        Returns:
            List of all offers
        """
        all_offers = []
        page = 1

        while True:
            offers = await self.get_offers(page=page)

            if not offers:
                break

            all_offers.extend(offers)

            if len(offers) < 12:  # Assuming 12 per page
                break

            page += 1

        return all_offers

    async def get_all_projects(
        self,
        max_pages: int = 5,
        categories: Optional[str] = None,
        price_to: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get all projects (paginated)

        Args:
            max_pages: Maximum number of pages to fetch
            categories: Category ID for filtering
            price_to: Maximum price for filtering

        Returns:
            List of all projects
        """
        all_projects = []

        for page in range(1, max_pages + 1):
            projects = await self.get_projects(page=page, categories=categories, price_to=price_to)

            if not projects:
                break

            all_projects.extend(projects)

        return all_projects

    async def __aenter__(self):
        """Async context manager entry"""
        proxies = {}
        if self.http_proxy:
            proxies["http://"] = self.http_proxy
        if self.https_proxy:
            proxies["https://"] = self.https_proxy
        if proxies:
            self._client = httpx.AsyncClient(timeout=self.timeout, proxies=proxies)
        else:
            self._client = httpx.AsyncClient(timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self._client:
            await self._client.aclose()

    @property
    def is_authenticated(self) -> bool:
        """Check if client is authenticated"""
        return self._token is not None

    @property
    def token(self) -> Optional[str]:
        """Get current authentication token"""
        return self._token
