import allure
import pytest

from niffler_tests.application import app
from niffler_tests.data.spendings import (
    amount,
    category,
    description,
    date_type_1,
    currency_usd,
    date_type_1_edit,
    description_edit,
    currency_rub,
    amount_edit,
    category_edit, bitcoin_spend_1, ethereum_spend_1, crypto_name, crypto_name_new, crypto_name_archive, username_edit,
)
from niffler_tests.data.user import (
    login_user,
    password_user,
    login_admin,
    password_admin, login_fail, password_fail,
)


from niffler_tests.marks import Pages, TestData

@allure.feature('Authentification')
class TestAuth:
    @allure.title('Тест успешной регистрации')
    @allure.story('Registration')
    def test_registration_successful(self):
        app.login_page.open()

        # WHEN
        app.login_page.create_new_account()
        app.registration_page.sign_up(login_user, password_user)

        # THEN
        app.registration_page.should_be_registered()

    @allure.story('Тест успешного логина')
    @allure.title('Вход в систему')
    def test_login_succcessful(self, add_admin):
        # WHEN
        app.login_page.login(login_admin, password_admin)

        # THEN
        app.main_page.should_be_logged_in()

    @allure.story('Logout')
    @allure.title('Тест успешного выхода из системы')
    @Pages.main_page
    def test_logout_successfull(self):

        # WHEN
        app.log_out()

        # THEN
        app.login_page.should_be_logged_out()

    @allure.story('Вход в систему')
    @allure.title('Тест логина с неправильным именем пользователя')
    def test_login_bad_username(self):
        # WHEN
        app.login_page.login(login_fail, password_admin)

        # THEN
        app.login_page.should_fail_to_log_in()

    @allure.story('Вход в систему')
    @allure.title('Тест логина с неправильным паролем')
    def test_login_bad_password(self):
        # WHEN
        app.login_page.login(login_admin, password_fail)

        # THEN
        app.login_page.should_fail_to_log_in()

@allure.feature('Spendings')
class TestSpenings():
    @allure.story('Добавление траты')
    @allure.title('Тест успешного добавления траты')
    @Pages.main_page
    def test_add_new_spending(self, spending_cleanup):

        # WHEN
        app.add_spending(amount, currency_usd, category, date_type_1, description)

        # THEN
        app.main_page.spending_should_have_data(
            category, amount, currency_usd, description
        )

    @allure.story('Добавление траты')
    @allure.title('Тест добавление траты с amount = 0')
    @Pages.main_page
    def test_add_spending_0_amount(self):
        # WHEN
        app.add_spending(currency=currency_usd, category=category, date=date_type_1, description=description)

        # THEN
        app.field_should_have_error('Amount has to be not less then 0.01')

    @allure.story('Добавление траты')
    @allure.title('Тест добавление траты без категории')
    @Pages.main_page
    def test_add_spending_without_category(self):
        # WHEN
        app.add_spending(amount=amount, currency=currency_usd, date=date_type_1, description=description)

        # THEN
        app.field_should_have_error('Please choose category')

    @allure.story('Добавление траты')
    @allure.title('Тест добавления траты с неправильной датой')
    @Pages.main_page
    def test_add_spending_without_date(self, spending_cleanup):
        """
        Bug UI: Uncaught RangeError: Invalid time value
             at Date.toISOString (<anonymous>)
        """

        # WHEN
        app.add_spending_without_date()

        # THEN
        app.field_should_have_error('Please choose date')

    @allure.story('Удаление траты')
    @allure.title('Тест удаления траты')
    @Pages.main_page
    @TestData.spends([bitcoin_spend_1])
    def test_delete_spending(self, spends):
        # WHEN
        app.main_page.delete_spending(category)

        # THEN
        app.main_page.spending_should_be_deleted(category)

    @allure.story('Удаление траты')
    @allure.title('Тест удаления множества трат')
    @Pages.main_page
    @TestData.spends([bitcoin_spend_1, ethereum_spend_1])
    def test_delete_multiple_spendings(self, spends):
        # WHEN
        app.main_page.delete_all_spendings()

        # THEN
        app.main_page.spending_should_be_deleted(category)

    @allure.story('Удаление траты')
    @allure.title('Тест редактирования траты')
    @Pages.main_page
    @TestData.spends([bitcoin_spend_1])
    def test_edit_spending(self, spends):
        # WHEN
        app.main_page.edit_spending()
        app.spending_page.update_spending_data(
            amount_edit, currency_rub, category_edit, date_type_1_edit, description_edit
        )

        # THEN
        app.main_page.spending_should_have_data(
            category_edit, amount_edit, currency_rub, description_edit
        )

    @allure.story('Удаление траты')
    @allure.title('Тест поиска траты')
    @Pages.main_page
    @TestData.spends([bitcoin_spend_1, ethereum_spend_1])
    def test_find_spending(self, spends):
        # WHEN
        app.main_page.find_spending(category)

        # THEN
        app.main_page.should_have_spending(category)

@allure.feature('Profile')
class TestProfile:
    @allure.story('Редактирование профиля')
    @allure.title('Тест Редактирования имени')
    @Pages.main_page
    def test_edit_profile(self):
        app.header.open_profile()

        # WHEN
        app.profile_page.change_name(username_edit)

        # THEN
        app.profile_page.name_should_be(username_edit)

@allure.feature('Category')
class TestCategory:
    @allure.story('Добавление категории')
    @allure.title('Тест успешного добавления категории')
    @Pages.main_page
    def test_add_category(self):
        app.header.open_profile()

        # WHEN
        app.profile_page.add_category(crypto_name)

        # THEN
        app.profile_page.should_have_category(crypto_name)

    @allure.story('Добавление категории')
    @allure.title('Тест добавления пустой категории')
    @Pages.main_page
    def test_add_empty_category(self):
        app.header.open_profile()

        # WHEN
        app.profile_page.add_empty_category()

        # THEN
        app.field_should_have_error('Allowed category length is from 2 to 50 symbols')

    @allure.story('Добавление категории')
    @allure.title('Тест добавления существующей категории')
    @Pages.main_page
    def test_add_existing_category(self):
        app.header.open_profile()

        # WHEN
        app.profile_page.add_category(category)

        # THEN
        app.alert_shows_error(f'Error while adding category {category}: Cannot save duplicates')

    @allure.story('Редактирование категории')
    @allure.title('Тест редактирования категории категории')
    @Pages.main_page
    def test_edit_category(self):
        app.header.open_profile()
        app.profile_page.add_category(crypto_name)

        # WHEN
        app.profile_page.edit_category(crypto_name, crypto_name_new)

        # THEN
        app.profile_page.should_have_category(crypto_name_new)

    @allure.story('Архив категорий')
    @allure.title('Тест архивирования категории')
    @Pages.main_page
    def test_archive_category(self):
        app.header.open_profile()
        app.profile_page.add_category(crypto_name)

        # WHEN
        app.profile_page.archive_category(crypto_name)

        # THEN
        app.profile_page.category_should_be_absent(crypto_name)

    @allure.story('Архив категорий')
    @allure.title('Тест разархивирования категории')
    @Pages.main_page
    def test_unarchive_category(self):
        app.header.open_profile()
        app.profile_page.add_category(crypto_name_archive)
        app.profile_page.archive_category(crypto_name_archive)

        # WHEN
        app.profile_page.unarchive_category(crypto_name_archive)

        # THEN
        app.profile_page.should_have_category(crypto_name_archive)