from urllib.parse import urljoin

import requests

from niffler_tests.utils.http_logger import log
from project import config


class AuthHttpClient:
    session: requests.Session
    auth_url: str = config.auth_url

    def __init__(self, auth_url: str):
        self.gateway_url = auth_url
        self.session = requests.session()
        # self.session.headers.update(
        #     {
        #         "Accept": "application/json",
        #         "Authorization": f"Bearer {token}",
        #         "Content-Type": "application/json",
        #     }
        # )

    # def log_in(self, username: str, password: str):
        # TODO implement Oauth2 login
        # https://blog.logto.io/ru/how-pkce-protects-the-authorization-code-flow-for-native-apps
        # https://chatgpt.com/c/690760df-a4ec-8330-a187-53a424a2f319
        # response = self.session.post(
        #     urljoin(self.gateway_url, "/login"), data=f'username={username}&password={password}'
        # )
        # log(response)
        # response.raise_for_status()
        # return response