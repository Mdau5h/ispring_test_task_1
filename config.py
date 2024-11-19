from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Config(BaseSettings):

    BASE_URL: str
    AUTH_LOGIN: str
    AUTH_PASS: str
    HEADLESS: bool = False


config = Config()
