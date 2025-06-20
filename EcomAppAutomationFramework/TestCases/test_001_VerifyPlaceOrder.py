import json
import pytest
from playwright.sync_api import Playwright

from EcomAppAutomationFramework.API_Utils.API_Factory import API_Factory
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from EcomAppAutomationFramework.PageObjects.cartPage import cartPage
from EcomAppAutomationFramework.PageObjects.checkoutPage import checkoutPage
from EcomAppAutomationFramework.PageObjects.orderDetailsPage import orderDetailsPage

productName = "ZARA COAT 3"

with open("EcomAppAutomationFramework/TestData/creds.json", "r") as file:
    test_data = json.load(file)
    users_data = test_data['user_credentials']

@pytest.mark.integration
@pytest.mark.parametrize('user_credentials', users_data)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):
    username = user_credentials['userEmail']
    password = user_credentials['userPassword']
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    DashboardPage = LoginPage.loginToApp(username,password)
    ProductDetailsPage = DashboardPage.click_product_view(productName)
    product_id = ProductDetailsPage.get_current_product_id()
    ProductDetailsPage.verify_product_is_visible(productName)
    OrdersPage = DashboardPage.navigate_to_orders()
    OrdersPage.delete_all_existing_orders()
    assert OrdersPage.verify_no_orders_present()
    apiFactory = API_Factory()
    orderID = apiFactory.createOrder(playwright, product_id, user_credentials)
    LoginPage.navigate_to_login()
    DashboardPage.navigate_to_orders()
    assert OrdersPage.verify_order_present(orderID)
    OrderDetailsPage = OrdersPage.click_view_button_for_order(orderID)
    OrderDetailsPage.verify_thank_you_message()

@pytest.mark.smoke
def test_place_order(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    DashboardPage = LoginPage.loginToApp("av1234@gmail.com", "Bulbul@123")
    product_name = "ZARA COAT 3"
    DashboardPage.add_product_to_cart(product_name)
    CartPage = DashboardPage.navigate_to_cart()
    assert CartPage.verify_product_in_cart(product_name)
    CheckoutPage = CartPage.proceed_to_checkout()
    CheckoutPage.enter_shipping_country("India")
    CheckoutPage.enter_payment_info()
    OrderDetailsPage = CheckoutPage.place_order()
    assert OrderDetailsPage.verify_successful_order_msg()
    order_id = OrderDetailsPage.get_order_id()

