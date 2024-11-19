from playwright.sync_api import Page, Response


class BasePage:
    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url

    def visit(self) -> Response | None:
        return self.page.goto(self.url, wait_until='domcontentloaded')

    def reload(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')
