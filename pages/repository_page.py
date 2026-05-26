from pages.base_page import BasePage


class RepositoryPage(BasePage):
    """GitHub Repository Page representation."""

    # Robust XPath combining multiple container structures (id or class) using XPath OR operator '|'
    README_CONTAINER_XPATH = (
        "//div[@id='readme'] | //article[contains(@class, 'markdown-body')]"
    )

    def is_readme_loaded(self) -> bool:
        """Verifies if the README container is loaded and visible.

        Uses a generous 10-second timeout to account for dynamic network loads on GitHub.
        """
        return self.is_element_visible(self.README_CONTAINER_XPATH, timeout=10000.0)

    def get_readme_text(self) -> str:
        """Retrieves all text content from the README markdown body."""
        return self.get_text_content(self.README_CONTAINER_XPATH)

    def is_copilotkit_text_visible_in_readme(self) -> bool:
        """Checks if the text 'CopilotKit' is visible inside the README body.

        Retrieves the readme text and performs a substring validation.
        """
        readme_text = self.get_readme_text()
        return "CopilotKit" in readme_text
