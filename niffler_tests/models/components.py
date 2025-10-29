from selene import browser

class Header:
    def __init__(self):
        self.button_spending = browser.element('[href="/spending"]')
        self.menu_account = browser.element('[data-testid="PersonIcon"]')

    def add_transaction(self):
        self.button_spending.click()

    def open_profile(self):
        self.menu_account.click()
        browser.element('[href="/profile"]').click()

