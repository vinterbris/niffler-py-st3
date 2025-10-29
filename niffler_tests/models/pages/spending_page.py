from selene import browser

class SpendingPage:
    def fill_transaction_data(self, amount, currency, category, date, description):
        browser.element('#amount').clear().type(amount)
        browser.element('#currency').click()
        browser.element(f'[data-value="{currency}"]').click()
        browser.element('#category').clear().type(category)
        browser.element('[name="date"]').clear().set_value(date)
        browser.element('#description').clear().type(description)

        browser.element('#save').click()