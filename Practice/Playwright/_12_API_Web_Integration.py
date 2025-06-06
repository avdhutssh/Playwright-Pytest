import time
from itertools import product

from playwright.sync_api import Playwright, expect

from _11_BaseAPI import API_Utils

productName = "ZARA COAT 3"

def test_ecom_API_Web(playwright:Playwright):
    #login to app
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("av1234@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Bulbul@123")
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
    for i in range(delete_count):
        delete_buttons.nth(0).click()
        time.sleep(1)
    print("✅ All existing orders deleted")

    expect(page.get_by_text("You have No Orders to show at")).to_be_visible()

    #create new order via API for product zara
    apiUtils=API_Utils()
    orderID = apiUtils.createOrder(playwright,productID)

    #verify order is created via UI
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click();
    expect(page.get_by_text(orderID)).to_be_visible()
    time.sleep(1)
    print(f"✅ Order created successfully with ID: {orderID}")



