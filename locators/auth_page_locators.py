from enum import StrEnum


class AuthPageEnum(StrEnum):
    LOGIN_FIELD = '//*[@id="login_field"]'
    PASS_FIELD = '//*[@id="password"]'
    SUBMIT_AUTH_BUTTON = '//*[@type="submit"]'
    DASHBOARD_CONTAINER = '//*[@id="dashboard"]'
