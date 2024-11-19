from playwright.sync_api import Page

from base.base_component import BaseComponent
from base.button import Button
from base.input import Input
from locators.auth_page_locators import AuthPageEnum


class LoginInput(Input):
    def __init__(self, page: Page) -> None:
        super().__init__(
            page=page,
            locator=AuthPageEnum.LOGIN_FIELD,
            name='Github login field'
        )


class PassInput(Input):
    def __init__(self, page: Page) -> None:
        super().__init__(
            page=page,
            locator=AuthPageEnum.PASS_FIELD,
            name='Github password field'
        )


class SubmitButton(Button):
    def __init__(self, page: Page) -> None:
        super().__init__(
            page=page,
            locator=AuthPageEnum.SUBMIT_AUTH_BUTTON,
            name='Github submit auth button',
        )


class DashboardContainer(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(
            page=page,
            locator=AuthPageEnum.DASHBOARD_CONTAINER,
            name='Github dashboard container',
            type_of='container'
        )
