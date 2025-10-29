from selene import browser, be


class LoginPage:
    def open(self):
        browser.open('/')

    def login(self, login, password):
        self.open()

        browser.element('[name="username"]').type(login)
        browser.element('[name="password"]').type(password)

        browser.element('.form__submit').click()

    def create_new_account(self):
        browser.element('.form__register').click()

    def should_be_logged_in(self):
        browser.element('[data-testid="PersonIcon"]').should(be.visible)
        browser.element('[href="/spending"]').should(be.visible)
        browser.element('#stat').should(be.visible)
        browser.element('#spendings').should(be.visible)
