from selene import browser, have


class RegistrationPage:
    def sign_up(self, login, password):
        browser.element("#username").type(login)
        browser.element("#password").type(password)
        browser.element("#passwordSubmit").type(password)
        browser.element(".form__submit").click()

    def should_be_registered(self):
        browser.element(".form__paragraph_success").should(
            have.text("Congratulations! You've registered!")
        )
