from urllib.parse import urljoin

import allure
import requests

from niffler_tests.utils.http_logger import log
from project import config


class SpendsHttpClient:
    session: requests.Session
    gateway_url: str = config.gateway_url

    def __init__(self, gateway_url: str, token: str):
        self.gateway_url = gateway_url
        self.session = requests.session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }
        )

    @allure.step('Добавить категорию')
    def add_category(self, name: str):
        response = self.session.post(
            urljoin(self.gateway_url, "/api/categories/add"), json={"name": name}
        )
        log(response)
        response.raise_for_status()
        return response.json()

    @allure.step('Получить категории')
    def get_categories(self):
        response = self.session.get(urljoin(self.gateway_url, "/api/categories/all"))
        log(response)
        response.raise_for_status()
        return response.json()

    @allure.step('Добавить трату')
    def add_spend(self, body):
        url = urljoin(self.gateway_url, '/api/spends/add')
        response = self.session.post(url, json=body)
        log(response)
        response.raise_for_status()
        return response.json()

    @allure.step('Удалить трату')
    def remove_spend(self, ids: list[int]):
        url = urljoin(self.gateway_url, '/api/spends/remove')
        response = self.session.delete(url, params={"ids": ids})
        log(response)
        response.raise_for_status()