import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Playwright, sync_playwright
import json

from EcomAppAutomationFramework.API_Utils.API_Factory import API_Factory
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from EcomAppAutomationFramework.PageObjects.orderDetailsPage import orderDetailsPage

# Import test data
with open("EcomAppAutomationFramework/TestData/creds.json", "r") as file:
    test_data = json.load(file)
    users_data = test_data['user_credentials']
    test_user = users_data[0]  # Take the first user for BDD tests

# Link the feature file
scenarios("../features/e2e.feature")

# Shared test context to store state between steps
class TestContext:
    def __init__(self):
        self.product_id = None
        self.order_id = None
        self.playwright = None
        self.browser_instance = None
        self.login_page = None
        self.dashboard_page = None
        self.product_details_page = None
        self.orders_page = None
        self.order_details_page = None

# Initialize context for each test run
@pytest.fixture(scope="function")
def context():
    return TestContext()

# Setup Playwright before test
@pytest.fixture(scope="function")
def setup_playwright(context):
    with sync_playwright() as playwright:
        context.playwright = playwright
        browser = playwright.chromium.launch(headless=False)
        context.browser_instance = browser.new_context().new_page()
        yield context
        context.browser_instance.close()

# Step Definitions

@given("I am logged into the application with valid credentials")
def login_with_valid_credentials(setup_playwright):
    context = setup_playwright
    login_page = loginPage(context.browser_instance)
    login_page.navigate_to_login()
    context.dashboard_page = login_page.loginToApp(test_user['userEmail'], test_user['userPassword'])
    context.login_page = login_page
    assert context.dashboard_page is not None

@when(parsers.parse('I select the product "{product_name}" for viewing'))
def select_product_for_viewing(setup_playwright, product_name):
    context = setup_playwright
    context.product_details_page = context.dashboard_page.click_product_view(product_name)
    assert context.product_details_page is not None

@when("I retrieve the product ID")
def retrieve_product_id(setup_playwright):
    context = setup_playwright
    context.product_id = context.product_details_page.get_current_product_id()
    assert context.product_id is not None and context.product_id != ""

@when("I verify the product is visible")
def verify_product_visible(setup_playwright):
    context = setup_playwright
    assert context.product_details_page.verify_product_is_visible("ZARA COAT 3")

@when("I navigate to orders page")
def navigate_to_orders(setup_playwright):
    context = setup_playwright
    context.orders_page = context.dashboard_page.navigate_to_orders()
    assert context.orders_page is not None

@when("I delete all existing orders")
def delete_all_orders(setup_playwright):
    context = setup_playwright
    context.orders_page.delete_all_existing_orders()

@when("I verify no orders are present")
def verify_no_orders(setup_playwright):
    context = setup_playwright
    assert context.orders_page.verify_no_orders_present()

@when("I create an order via API using the product ID")
def create_order_via_api(setup_playwright):
    context = setup_playwright
    api_factory = API_Factory()
    context.order_id = api_factory.createOrder(context.playwright, context.product_id, test_user)
    assert context.order_id is not None and context.order_id != ""

@when("I navigate back to login page")
def navigate_back_to_login(setup_playwright):
    context = setup_playwright
    context.login_page.navigate_to_login()

@then("I should see my order in the orders list")
def verify_order_in_list(setup_playwright):
    context = setup_playwright
    assert context.orders_page.verify_order_present(context.order_id)

@then("I can view the order details")
def view_order_details(setup_playwright):
    context = setup_playwright
    context.order_details_page = context.orders_page.click_view_button_for_order(context.order_id)
    assert context.order_details_page is not None

@then("I should see the thank you message")
def verify_thank_you_message(setup_playwright):
    context = setup_playwright
    assert context.order_details_page.verify_thank_you_message() 