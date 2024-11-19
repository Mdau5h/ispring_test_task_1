import sys
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()
args = sys.argv[1:]

headless = True
if '--headed' in args:
    headless = False


class Config(BaseSettings):

    BASE_URL: str
    AUTH_LOGIN: str
    AUTH_PASS: str
    HEADLESS: bool = headless


config = Config()
