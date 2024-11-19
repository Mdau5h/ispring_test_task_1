from playwright.sync_api import Page, expect

from base.base_component import BaseComponent


class Button(BaseComponent):
    def __init__(self, name: str, page: Page, locator: str, type_of="button"):
        super().__init__(page, locator, name, type_of)
        self.name = name
        self.type_of = type_of

    def hover(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.hover()

    def double_click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.dblclick()

    def should_be_enabled(self, timeout=15000, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).not_to_be_disabled(timeout=timeout)

    def should_be_disabled(self, timeout=15000, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled(timeout=timeout)
