import allure
from selene import browser, have
from selenium.webdriver.common.keys import Keys

from niffler_tests.data.spendings import category


class SpendingPage:
    def __init__(self):
        self.button_add = browser.element("#save")
        self.field_description = browser.element("#description")
        self.field_date = browser.element('[name="date"]')
        self.field_category = browser.element("#category")
        self.field_currentcy = browser.element("#currency")
        self.field_amount = browser.element("#amount")

    def drop_down_list_currency(self, value):
        return browser.element(f'[data-value="{value}"]')

    @allure.step('Заполнить данные траты')
    def fill_spending_data(self, amount, currency, category, date, description):
        if amount:
            self.field_amount.type(amount)
        self.field_currentcy.click()
        self.drop_down_list_currency(currency).click()
        if category:
            browser.element("#category").type(category)
        self.field_date.set_value(date)
        self.field_description.type(description)

        self.button_add.click()

    @allure.step('Заполнить данные трады без даты')
    def fill_spending_data_without_date(self):
        self.field_amount.type('1')
        self.field_category.type(category)
        self.field_date.click().send_keys(Keys.DELETE)

        self.button_add.click()

    @allure.step('Обновить данные траты')
    def update_spending_data(self, amount, currency, category, date, description):
        self.field_amount.clear().type(amount)
        self.field_currentcy.click()
        browser.element(f'[data-value="{currency}"]').click()
        browser.element("#category").clear().type(category)
        self.field_date.clear().set_value(date)
        self.field_description.clear().type(description)

        self.button_add.click()



