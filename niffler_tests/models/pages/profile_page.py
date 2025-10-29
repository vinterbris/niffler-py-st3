from selene import browser, have, be


class ProfilePage:
    def change_name(self, value):
        browser.element('#name').clear()
        browser.element('#name').type(value)
        browser.element('[type="submit"]').click()

    def name_should_be(self, value):
        browser.element('#name').should(have.value(value))

    def add_category(self, name):
        browser.element('#category').type(name).press_enter()

    def edit_category(self, name, new_name):
        browser.all('[role="button"]').element_by(have.exact_text(name)).element('..').element('[aria-label="Edit category"]').click()

        browser.element(f'[value="{name}"]').clear().type(new_name)
        browser.element(f'[value="{new_name}"]').press_enter()

    def archive_category(self, name):
        browser.all('[role="button"]').element_by(have.exact_text(name)).element('..').element('[aria-label="Archive category"]').click()

        browser.element('[role="dialog"]').all('[type="button"]').element_by(have.exact_text('Archive')).click()

    def should_have_category(self, name):
        browser.all('[role="button"]').element_by(have.exact_text(name)).should(be.present)

    def category_should_be_archived(self, name):
        browser.all('[role="button"]').element_by(have.exact_text(name)).should(be.absent)