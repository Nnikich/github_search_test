from pages.base_page import BasePage


class MainPage(BasePage):
    """GitHub Main Page representation."""

    URL = "https://github.com"

    # Robust XPath locators using logical OR, partial attribute matching and tag selectors
    SEARCH_TRIGGER_XPATH = (
        "//button[contains(@class, 'header-search-button') "
        "or @data-target='qbsearch-input.inputButton' "
        "or contains(., 'Search')]"
    )
    SEARCH_INPUT_XPATH = (
        "//input[@id='query-builder-test' "
        "or @name='q' "
        "or contains(@placeholder, 'Search') "
        "or contains(@class, 'query-builder-input')]"
    )

    def open(self) -> None:
        """Opens the GitHub home page."""
        self.navigate(self.URL)

    def search_for(self, query: str) -> None:
        """Triggers the search box, enters the search query, and submits it by pressing Enter."""
        # Check if we need to click the search trigger button (modern GitHub header has a search overlay)
        if self.is_element_visible(self.SEARCH_TRIGGER_XPATH, timeout=5000):
            self.click_element(self.SEARCH_TRIGGER_XPATH)

        # Wait for search input to be active, fill the search query, and press Enter
        self.fill_element(self.SEARCH_INPUT_XPATH, query)
        self.press_key(self.SEARCH_INPUT_XPATH, "Enter")
