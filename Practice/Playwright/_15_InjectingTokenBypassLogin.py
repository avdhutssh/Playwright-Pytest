import time

from playwright.sync_api import Playwright, expect

from _11_BaseAPI import API_Utils


def test_injectingTokenBypassLogin(playwright:Playwright):
    apiUtils = API_Utils()
    accessToken = apiUtils.getToken(playwright)
    print(f"Access Token: {accessToken}")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token', '{accessToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
    time.sleep(1)
    print("✅ Successfully bypassed login using injected token")