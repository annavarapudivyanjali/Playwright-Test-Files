
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright


BASE_DIR = Path(__file__).resolve().parent
PROFILE_DIR = BASE_DIR / "playwright_profile"


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            viewport={"width": 1440, "height": 900},
        )

        yield context

        context.close()


@pytest.fixture
def teams_page(browser_context):
    page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

    yield page

    # Keep the persistent browser context alive for the test session.

