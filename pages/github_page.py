from playwright.sync_api import Page
from base.base_page import BasePage
from components.github_page import (
    LoginInput,
    PassInput,
    SubmitButton,
    DashboardContainer
)


class GithubPage(BasePage):
    def __init__(self, page: Page, url: str) -> None:
        super().__init__(page, url)
        self.login_field = LoginInput(page)
        self.pass_field = PassInput(page)
        self.submit_button = SubmitButton(page)
        self.dashboard_container = DashboardContainer(page)
