from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.repository_page import RepositoryPage


def test_github_search_and_navigate_to_copilotkit(
    main_page: MainPage,
    search_results_page: SearchResultsPage,
    repository_page: RepositoryPage,
) -> None:
    """Verifies that a user can search for 'copilot' on GitHub, navigate to

    the CopilotKit repository, and successfully view its README content.
    """
    # Step 1: Open the GitHub home page
    main_page.open()

    # Step 2: Search for 'copilot' and submit
    main_page.search_for("copilot")

    # Step 3: Find and click the 'CopilotKit' repository link in the results
    search_results_page.click_repository_link()

    # Step 4: Wait for the navigation to complete and verify the URL
    main_page.page.wait_for_url("**/CopilotKit/CopilotKit", timeout=15000)
    current_url = main_page.page.url
    assert "CopilotKit/CopilotKit" in current_url, (
        f"Expected to navigate to repository containing 'CopilotKit/CopilotKit', "
        f"but currently at: '{current_url}'"
    )

    # Step 5: Verify the README.md is visible and contains the text 'CopilotKit'
    assert repository_page.is_readme_loaded(), "README.md section was not loaded on the page."
    
    assert repository_page.is_copilotkit_text_visible_in_readme(), (
        "Text 'CopilotKit' was not found inside the README.md content section."
    )
