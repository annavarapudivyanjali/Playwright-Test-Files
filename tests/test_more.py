from playwright.sync_api import Page, expect
def test_homepage_title(page: Page):

    page.goto("https://teams.cloud.microsoft/")

    expect(page).to_have_title("Microsoft Teams")
    