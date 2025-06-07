
import time
from playwright.sync_api import Page, Playwright, expect

from _11_BaseAPI import API_Utils

mockResponse = {"data":[],"message":"No Orders"}

def interceptResponse(route):
    print(f"Intercepted URL: {route.request.url}")
    route.fulfill(json=mockResponse)

def test_InterceptResponse(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    apiUtils=API_Utils()
    apiUtils.createOrder(playwright)
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", interceptResponse)
    page.get_by_placeholder("email@example.com").fill("av1234@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Bulbul@123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="ORDERS")).to_be_visible()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(1)
    order_text = page.locator(".mt-4").text_content()
    print(f"Order text: {order_text}")
    assert "You have No Orders to show at this time. Please Visit Back Us" in order_text
    print("✅ Intercepted response successfully")

