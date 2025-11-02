import allure

from niffler_tests.models.components.header import Header
from niffler_tests.models.pages.login_page import LoginPage
from niffler_tests.models.pages.main_page import MainPage
from niffler_tests.models.pages.profile_page import ProfilePage
from niffler_tests.models.pages.registration_page import RegistrationPage
from niffler_tests.models.pages.spending_page import SpendingPage
from selene import browser, have


class Application:
    def __init__(self):
        self.login_page = LoginPage()
        self.registration_page = RegistrationPage()
        self.main_page = MainPage()
        self.spending_page = SpendingPage()
        self.profile_page = ProfilePage()

        self.header = Header()

    @allure.step('Добавить трату')
    def add_spending(self, amount=None, currency=None, category=None, date=None, description=None):
        self.header.add_transaction()
        self.spending_page.fill_spending_data(
            amount, currency, category, date, description
        )

    @allure.step('Добавить трату без даты')
    def add_spending_without_date(self):
        self.header.add_transaction()
        self.spending_page.fill_spending_data_without_date()

    @allure.step('Выйти из системы')
    def log_out(self):
        self.header.sign_out()
        browser.element('[role="dialog"]').all('[type="button"]').element_by(have.exact_text('Log out')).click()

    @allure.step('Поле должно отображать ошибку')
    def field_should_have_error(self, value):
        browser.element('.input__helper-text').should(have.text(value))

    @allure.step('Алерт должен отображать ошибку')
    def alert_shows_error(self, value):
        browser.element('[role="alert"]').element('.MuiAlert-message').should(have.text(value))

app = Application()
