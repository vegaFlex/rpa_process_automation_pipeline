class LoginError(Exception):
    """Raised when login fails."""


class NavigationError(Exception):
    """Raised when page navigation or verification fails."""


class ProcessingError(Exception):
    """Raised when raw or processed data handling fails."""


class ReportingError(Exception):
    """Raised when report generation fails."""
