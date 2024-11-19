import pytest
from playwright.sync_api import Page, sync_playwright
from pages.github_page import GithubPage
from config import config


@pytest.fixture(scope='function')
def open_browser() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=config.HEADLESS, args=["--start-maximized"])
        context = chromium.new_context(no_viewport=True)
        page = context.new_page()

        def log_console_message(msg):
            print(f'Browser console: {msg.type}: {msg.text}')

        page.on('console', log_console_message)
        yield page
        chromium.close()


@pytest.fixture(scope='function')
def github_page(open_browser: Page) -> GithubPage:
    return GithubPage(open_browser, config.BASE_URL)
