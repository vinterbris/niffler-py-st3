from typing import Optional

import dotenv
import pydantic_settings

from niffler_tests.utils import supported_browsers


class Config(pydantic_settings.BaseSettings):
    """
    Automatically loads values from .env for corresponding fields
    """
    base_url: str = None
    auth_url: str = None
    gateway_url: str = None
    user_login: str = None
    user_password: str = None

    timeout: float = 5.0
    browser_name: supported_browsers.BrowserName = 'chrome'
    headless: bool = False
    window_width: int = 1600
    window_height: int = 1300

    selenoid: bool = False
    browser_version: str = '127.0'
    selenoid_url: str = 'http://localhost:4444'

    remote_enableVNC: bool = True
    remote_enableVideo: bool = True

    save_page_source_on_failure: bool = True

    login: Optional[str] = None
    password: Optional[str] = None


config = Config(_env_file=dotenv.find_dotenv())

if __name__ == '__main__':
    """
    Run python3 project.py to check config values on start. Used for debugging
    """
    print(config.__repr__())