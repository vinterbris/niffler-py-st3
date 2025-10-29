from niffler_tests.models.components import Header
from niffler_tests.models.pages.login_page import LoginPage
from niffler_tests.models.pages.main_page import MainPage
from niffler_tests.models.pages.profile_page import ProfilePage
from niffler_tests.models.pages.registration_page import RegistrationPage
from niffler_tests.models.pages.spending_page import SpendingPage


class Application:
    def __init__(self):
        self.login_page = LoginPage()
        self.registration_page = RegistrationPage()
        self.main_page = MainPage()
        self.spending_page = SpendingPage()
        self.profile_page = ProfilePage()

        self.header = Header()

    def add_spending(self, amount, currency, category, date, description):
        self.header.add_transaction()
        self.spending_page.fill_transaction_data(amount, currency, category, date, description)

app = Application()