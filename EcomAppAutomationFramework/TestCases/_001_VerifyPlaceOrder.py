import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from EcomAppAutomationFramework.API_Utils.API_Factory import API_Factory

productName = "ZARA COAT 3"

with open("EcomAppAutomationFramework/TestData/creds.json", "r") as file:
    test_data = json.load(file)
    print(test_data)
    users_data = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials',users_data)
def test_e2e_web_api(playwright:Playwright, user_credentials):
    username = user_credentials['userEmail']
    password = user_credentials['userPassword']

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(username)
    page.get_by_placeholder("enter your passsword").fill(password)
    page.get_by_role("button", name="Login").click()
    expect( page.get_by_role("button", name="ORDERS")).to_be_visible()
    print("✅ Logged in successfully")

    #get the product id for zara
    page.locator(f"//*[normalize-space(text())='{productName}']/../..//button[normalize-space(text())='View']").click()
    productURL = page.url
    print(f"✅ Product URL: {productURL}")
    productID = productURL.split("/")[-1]
    print(f"✅ Product ID for {productName} is : {productID}")
    expect(page.get_by_text("ZARA COAT 3")).to_be_visible()

    #delete existing orders if present
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(2)
    delete_buttons = page.locator("button.btn-danger")
    delete_count = delete_buttons.count()
    print(f"Number of delete buttons found: {delete_count}")
    while page.locator("button.btn-danger").count() > 0:
        page.locator("button.btn-danger").first.click()
        page.wait_for_timeout(1000)
    print("✅ All existing orders deleted")

    expect(page.get_by_text("You have No Orders to show at")).to_be_visible()

    #create new order via API for product zara
    apiFactory=API_Factory()
    orderID = apiFactory.createOrder(playwright,productID)

    #verify order is created via UI
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click();
    expect(page.get_by_text(orderID)).to_be_visible()
    time.sleep(1)
    print(f"✅ Order created successfully with ID: {orderID}")

    # orders History page-> order is present
    orderRow = page.locator("tr").filter(has_text=orderID)
    orderRow.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print("✅ Order details page is displayed")
    context.close()


