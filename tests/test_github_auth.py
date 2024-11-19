from pages.github_page import GithubPage
from config import config


class TestAuth:

    def test_github_auth(self, github_page: GithubPage):

        github_page.visit()
        github_page.login_field.fill(config.AUTH_LOGIN)
        github_page.pass_field.fill(config.AUTH_PASS)

        with (github_page.page.expect_response(
                lambda response: "session" in response.url and response.request.method == "POST") as response_info):
            github_page.submit_button.click()
            assert response_info.value.status == 302

        github_page.dashboard_container.should_exist()
        github_page.dashboard_container.should_be_visible()

    def test_github_auth_negative(self, github_page: GithubPage):

        github_page.visit()
        github_page.login_field.fill('ogwoefgseufg')
        github_page.pass_field.fill('wrong_pass')

        with (github_page.page.expect_response(
                lambda response: "session" in response.url and response.request.method == "POST") as response_info):
            github_page.submit_button.click()
            assert response_info.value.status == 200

        github_page.dashboard_container.should_not_exist()
        github_page.dashboard_container.should_not_be_visible()
