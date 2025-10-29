from niffler_tests.application import app
from niffler_tests.data.spendings import amount, category, description, date_type_1, currency_usd, \
    date_type_1_edit, description_edit, currency_rub, amount_edit, category_edit
from niffler_tests.data.user import login_user, password_user, login_admin, password_admin
from faker import Faker

fake = Faker()

# def test_new():
#     import requests
#     base_url = 'http://auth.niffler.dc:9000'
#     response = requests.get(base_url + '/login')
#     # xsrf_token = response.cookies['XSRF-TOKEN']
#     # jsession_token = response.cookies['JSESSIONID']
#
#
#     url = 'http://auth.niffler.dc:9000/register'
#     headers = {
#         'Cookie': 'XSRF-TOKEN=21ec575c-0a1d-490a-a665-8c03c064aaed'
#     }
#     data = f'_csrf={xsrf_token}&uusername=admin&password=adminadmin'
#     # data = 'username=admin&password=adminadmin&passwordSubmit=adminadmin'
#
#     response = requests.post(url, data=data, headers=headers)
#     print(response.status_code)



def test_registration_successful():
    app.login_page.open()

    # WHEN
    app.login_page.create_new_account()
    app.registration_page.sign_up(login_user, password_user)

    # THEN
    app.registration_page.should_be_registered()


def test_login_succcessful(add_admin):

    # WHEN
    app.login_page.login(login_admin, password_admin)

    # THEN
    app.login_page.should_be_logged_in()


def test_add_new_spending(spending_cleanup):
    app.login_page.login(login_admin, password_admin)

    # WHEN
    app.add_spending(amount, currency_usd, category, date_type_1, description)

    # THEN
    app.main_page.transaction_should_have_data(category, amount, currency_usd, description)

def test_delete_spending():
    app.login_page.login(login_admin, password_admin)
    app.add_spending(amount, currency_usd, category, date_type_1, description)

    # WHEN
    app.main_page.delete_transaction(category)

    # THEN
    app.main_page.transaction_should_be_deleted(category)


def test_edit_spending(spending_setup):

    # WHEN
    app.main_page.edit_spending()
    app.spending_page.fill_transaction_data(amount_edit, currency_rub, category_edit, date_type_1_edit, description_edit)

    # THEN
    app.main_page.transaction_should_have_data(category_edit, amount_edit, currency_rub, description_edit)

def test_find_spending(double_spending_setup):

    # WHEN
    app.main_page.find_transaction(category)

    # THEN
    app.main_page.should_have_transaction(category)

def test_edit_profile():
    app.login_page.login(login_admin, password_admin)
    app.header.open_profile()

    # WHEN
    app.profile_page.change_name('Админ')

    # THEN
    app.profile_page.name_should_be('Админ')


def test_add_category():
    app.login_page.login(login_admin, password_admin)
    app.header.open_profile()

    crypto = fake.cryptocurrency_name()

    # WHEN
    app.profile_page.add_category(crypto)

    # THEN
    app.profile_page.should_have_category(crypto)

def test_edit_category():
    app.login_page.login(login_admin, password_admin)
    app.header.open_profile()

    crypto = fake.cryptocurrency_name()
    crypto_new = fake.cryptocurrency_name()
    app.profile_page.add_category(crypto)

    # WHEN
    app.profile_page.edit_category(crypto, crypto_new)

    # THEN
    app.profile_page.should_have_category(crypto_new)

def test_archive_category():
    app.login_page.login(login_admin, password_admin)
    app.header.open_profile()

    crypto = fake.cryptocurrency_name()
    app.profile_page.add_category(crypto)

    # WHEN
    app.profile_page.archive_category(crypto)

    # THEN
    app.profile_page.category_should_be_archived(crypto)