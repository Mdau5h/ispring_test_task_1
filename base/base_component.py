from playwright.sync_api import Locator, Page, expect


class BaseComponent:
    def __init__(self, page: Page, locator: str, name: str, type_of: str) -> None:
        self.page = page
        self.name = name
        self.type_of = type_of
        self.locator = locator

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def click(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.click()

    def should_be_visible(self, timeout=15000, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible(timeout=timeout)

    def should_not_be_visible(self, timeout=15000, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).not_to_be_visible(timeout=timeout)

    def should_exist(self, timeout=15000, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_attached(timeout=timeout)

    def should_not_exist(self, timeout=15000, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).not_to_be_attached(timeout=timeout)

    def should_have_text(self, value: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(value)
