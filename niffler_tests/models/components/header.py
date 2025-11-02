from selene import browser, have


class Header:
    def __init__(self):
        self.button_spending = browser.element('[href="/spending"]')
        self.menu_account = browser.element('[data-testid="PersonIcon"]')

    def add_transaction(self):
        self.button_spending.click()

    def open_profile(self):
        self.menu_account.click()
        browser.element('[href="/profile"]').click()

    def open_profile_menu(self):
        self.menu_account.click()

    def sign_out(self):
        self.open_profile_menu()
        browser.element('[role="menu"]').all('li').element_by(have.exact_text('Sign out')).click()