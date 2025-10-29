import allure_commons
import pytest
from selene import browser, support, Browser
from selenium import webdriver

import project
from niffler_tests.application import app
from niffler_tests.data.spendings import amount, currency_usd, category, date_type_1, description, category_edit, \
    amount_edit, currency_rub, description_edit
from niffler_tests.data.user import login_admin, password_admin
from niffler_tests.utils import attach, supported_browsers


@pytest.fixture(scope='session', autouse=True)
def add_reporting_to_selene_steps():
    """
    Code from https://github.com/yashaka/python-web-test
    :return:
    """

    from niffler_tests.plugins.python import monkey

    original_open = Browser.open

    @monkey.patch_method_in(Browser)
    def open(self, relative_or_absolute_url: str):
        from niffler_tests.plugins.allure import report

        return report.step(original_open)(self, relative_or_absolute_url)

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = project.config.base_url
    browser.config.timeout = project.config.timeout
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.save_page_source_on_failure = (
        project.config.save_page_source_on_failure
    )
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    if project.config.browser_name == supported_browsers.chrome:
        options = webdriver.ChromeOptions()

    if project.config.browser_name == supported_browsers.firefox:
        options = webdriver.FirefoxOptions()

    if project.config.headless:
        options.add_argument('--headless=new')

    options.page_load_strategy = 'eager'

    if project.config.selenoid:
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-application-cache')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        selenoid_capabilities = {
            "browserName": project.config.browser_name,
            "browserVersion": project.config.browser_version,
            "selenoid:options": {
                "enableVideo": project.config.remote_enableVideo,
            },
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=project.config.selenoid_url + '/wd/hub', options=options
        )

        browser.config.driver = driver
    else:
        browser.config.driver_options = options

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, project.config.selenoid_url)

    browser.quit()

@pytest.fixture
def add_admin():
    app.login_page.open()
    app.login_page.create_new_account()
    app.registration_page.sign_up(login_admin, password_admin)

@pytest.fixture
def spending_setup():
    app.login_page.login(login_admin, password_admin)
    app.add_spending(amount, currency_usd, category, date_type_1, description)

    yield

    app.main_page.delete_all_transactions()

@pytest.fixture
def double_spending_setup():
    app.login_page.login(login_admin, password_admin)
    app.add_spending(amount, currency_usd, category, date_type_1, description)
    app.add_spending(amount_edit, currency_rub, category_edit, date_type_1, description_edit)

    yield

    app.main_page.delete_all_transactions()

@pytest.fixture
def spending_cleanup():
    yield

    app.main_page.delete_all_transactions()
