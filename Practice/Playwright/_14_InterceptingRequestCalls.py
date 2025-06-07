
import time
from playwright.sync_api import Page, Playwright, expect


def interceptRequest(route):
    print(f"Intercepted URL: {route.request.url}")
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/12345")

def test_InterceptRequestCall(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("av1234@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Bulbul@123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="ORDERS")).to_be_visible()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(1)
    errMessage = page.locator(".blink_me").text_content()
    print(errMessage)
    assert errMessage == "You are not authorize to view this order"
    print("✅ Intercepted request successfully")

