"""
Custom exceptions for Kwork API
"""


class KworkAPIError(Exception):
    """Base exception for Kwork API errors"""
    pass


class KworkAuthError(KworkAPIError):
    """Exception raised for authentication errors"""
    pass


class KworkRequestError(KworkAPIError):
    """Exception raised for request errors"""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response
