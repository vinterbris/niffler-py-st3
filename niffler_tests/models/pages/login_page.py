import allure
from selene import browser, be, have


class LoginPage:
    def __init__(self):
        self.field_login = browser.element('[name="username"]')
        self.field_password = browser.element('[name="password"]')
        self.button_submit = browser.element(".form__submit")
        self.button_create_new_account = browser.element(".form__register")

    @allure.step('Открыть сайт')
    def open(self):
        browser.open("/")

    @allure.step('Войти в систему')
    def login(self, login=None, password=None):
        self.open()

        self.field_login.type(login)
        self.field_password.type(password)

        self.button_submit.click()

    @allure.step('Нажать кнопку Create new account')
    def create_new_account(self):
        self.button_create_new_account.click()

    @allure.step('Должен быть разлогинен')
    def should_be_logged_out(self):
        browser.element('[class="header"]').should(have.text('Log in'))
        self.field_login.should(be.present)
        self.field_password.should(be.present)
        self.button_submit.should(be.present)
        self.button_create_new_account.should(be.present)

    @allure.step('Должен показывать ошибку Bad credentials')
    def should_fail_to_log_in(self):
        browser.element('.form__error').should(have.text('Bad credentials'))
