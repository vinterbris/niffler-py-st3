import allure
from selene import browser, have, be, command


class MainPage:
    @allure.step('Отредактировать трату')
    def edit_spending(self):
        browser.element('[aria-label="Edit spending"]').click()

    @allure.step('Найти трату')
    def find_spending(self, category):
        browser.element('[placeholder="Search"]').type(category).press_enter()

    @allure.step('Удалить трату')
    def delete_spending(self, category):
        browser.all(".MuiTableCell-root").element_by(have.text(category)).click()

        browser.element("#delete").click()
        browser.element('[role="dialog"]').all('[type="button"]').element_by(
            have.text("Delete")
        ).click()

    @allure.step('Удалить все траты')
    def delete_all_spendings(self):
        browser.element('[aria-label="select all rows"]').perform(command.js.click)

        browser.element("#delete").click()
        browser.element('[role="dialog"]').all('[type="button"]').element_by(
            have.text("Delete")
        ).click()

    @allure.step('Трата должна быть удалена')
    def spending_should_be_deleted(self, category):
        browser.all(".MuiTableCell-root").element_by(have.text(category)).with_(
            timeout=4.0
        ).should(be.absent)
        browser.all("//div//p").element_by(have.text("There are no spendings")).should(
            be.present
        )

    @allure.step('Трата должна содержать данные')
    def spending_should_have_data(self, category, amount, currency, description):
        if currency == "USD":
            currency = "$"
        elif currency == "RUB":
            currency = "₽"

        browser.all("//tbody//tr").should(have.size(1))
        browser.all(".MuiTableCell-root").element_by(have.text(category)).should(
            be.present
        )
        browser.all(".MuiTableCell-root").element_by(
            have.text(f"{amount} {currency}")
        ).should(be.present)
        browser.all(".MuiTableCell-root").element_by(have.text(description)).should(
            be.present
        )

    @allure.step('Должна быть трата')
    def should_have_spending(self, category):
        browser.all("//tbody//tr").should(have.size(1))
        browser.all(".MuiTableCell-root").element_by(have.text(category)).should(
            be.present
        )

    @allure.step('Должен быть разлогинен')
    def should_be_logged_in(self):
        browser.element('[data-testid="PersonIcon"]').should(be.visible)
        browser.element('[href="/spending"]').should(be.visible)
        browser.element("#stat").should(be.visible)
        browser.element("#spendings").should(be.visible)
