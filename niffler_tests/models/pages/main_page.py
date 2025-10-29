from selene import browser, have, be, command


class MainPage:
    def edit_spending(self):
        browser.element('[aria-label="Edit spending"]').click()

    def find_transaction(self, category):
        browser.element('[placeholder="Search"]').type(category).press_enter()

    def delete_transaction(self, category):
        browser.all('.MuiTableCell-root').element_by(have.text(category)).click()

        browser.element('#delete').click()
        browser.element('[role="dialog"]').all('[type="button"]').element_by(have.text('Delete')).click()

    def delete_all_transactions(self):
        browser.element('[aria-label="select all rows"]').perform(command.js.click)

        browser.element('#delete').click()
        browser.element('[role="dialog"]').all('[type="button"]').element_by(have.text('Delete')).click()

    def transaction_should_be_deleted(self, category):
        browser.all('.MuiTableCell-root').element_by(have.text(category)).with_(timeout=4.0).should(be.absent)
        browser.all('//div//p').element_by(have.text('There are no spendings')).should(be.present)

    def transaction_should_have_data(self, category, amount, currency, description):
        if currency == 'USD':
            currency = '$'
        elif currency == 'RUB':
            currency = '₽'

        browser.all('//tbody//tr').should(have.size(1))
        browser.all('.MuiTableCell-root').element_by(have.text(category)).should(be.present)
        browser.all('.MuiTableCell-root').element_by(have.text(f'{amount} {currency}')).should(be.present)
        browser.all('.MuiTableCell-root').element_by(have.text(description)).should(be.present)

    def should_have_transaction(self, category):
        browser.all('//tbody//tr').should(have.size(1))
        browser.all('.MuiTableCell-root').element_by(have.text(category)).should(be.present)