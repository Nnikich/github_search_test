from playwright.sync_api import Page, Locator


class BasePage:
    """Base Page class containing common page operations and utilities."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigates to the specified URL."""
        self.page.goto(url)

    def find_element(self, selector: str) -> Locator:
        """Finds a locator using the specified selector (XPath or CSS)."""
        return self.page.locator(selector)

    def click_element(self, selector: str, timeout: float = 10000.0) -> None:
        """Clicks an element found by selector after waiting for it to be visible."""
        element = self.find_element(selector)
        element.wait_for(state="visible", timeout=timeout)
        element.click()

    def fill_element(self, selector: str, text: str, timeout: float = 10000.0) -> None:
        """Fills an input element with text after waiting for it to be visible."""
        element = self.find_element(selector)
        element.wait_for(state="visible", timeout=timeout)
        element.fill(text)

    def press_key(self, selector: str, key: str, timeout: float = 10000.0) -> None:
        """Presses a specific key on an element (e.g. 'Enter')."""
        element = self.find_element(selector)
        element.wait_for(state="visible", timeout=timeout)
        element.press(key)

    def get_text_content(self, selector: str, timeout: float = 10000.0) -> str:
        """Returns the text content of an element."""
        element = self.find_element(selector)
        element.wait_for(state="visible", timeout=timeout)
        return element.text_content() or ""

    def is_element_visible(self, selector: str, timeout: float = 5000.0) -> bool:
        """Checks if an element is visible within the timeout period."""
        try:
            element = self.find_element(selector)
            element.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False
