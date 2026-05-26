import pytest
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.repository_page import RepositoryPage


@pytest.fixture(scope="session")
def browser_channel():
    """Forces Playwright to launch Google Chrome instead of Chromium."""
    return "chrome"


@pytest.fixture
def browser_context_args(browser_context_args):
    """Overrides default browser context arguments to set a desktop viewport."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }


@pytest.fixture
def main_page(page: Page) -> MainPage:
    """Fixture to initialize the GitHub Main Page object."""
    return MainPage(page)


@pytest.fixture
def search_results_page(page: Page) -> SearchResultsPage:
    """Fixture to initialize the GitHub Search Results Page object."""
    return SearchResultsPage(page)


@pytest.fixture
def repository_page(page: Page) -> RepositoryPage:
    """Fixture to initialize the GitHub Repository Page object."""
    return RepositoryPage(page)
