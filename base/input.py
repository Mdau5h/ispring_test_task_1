from playwright.sync_api import expect, Page

from base.base_component import BaseComponent


class Input(BaseComponent):
    def __init__(self, name: str, page: Page, locator: str, type_of="input_field"):
        super().__init__(page, locator, name, type_of)
        self.name = name
        self.type_of = type_of

    def fill(self, value: str, validate_value=False, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.fill(value)
        if validate_value:
            self.should_have_value(value, **kwargs)

    def should_have_value(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
