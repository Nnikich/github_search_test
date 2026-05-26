from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """GitHub Search Results Page representation."""

    # Highly robust and precise XPath that:
    # 1. Matches the main repository link href exactly OR partially,
    # 2. Uses logical NOT and contains() to prevent strict-mode violations (excluding secondary links like stargazers),
    # 3. Ensures the element is within a search-result container or has the appropriate component attributes.
    COPILOTKIT_REPO_LINK_XPATH = (
        "//a[(@href='/CopilotKit/CopilotKit' "
        "or (contains(@href, '/CopilotKit/CopilotKit') "
        "and not(contains(@href, '/stargazers')) "
        "and not(contains(@href, '/forks')))) "
        "and (ancestor::div[contains(@class, 'search-result')] "
        "or @data-component='Link')]"
    )

    def click_repository_link(self) -> None:
        """Clicks the CopilotKit repository link in the search results."""
        self.click_element(self.COPILOTKIT_REPO_LINK_XPATH)
