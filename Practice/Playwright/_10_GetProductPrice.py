from playwright.sync_api import Page, expect

PRODUCT_NAME = "Rice"

def test_GetProductPrice(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceValue = index
            print(f"✅ Found 'Price' column at index: {priceValue}")
            break

    expect(page.locator("tr").filter(has_text=PRODUCT_NAME).locator("td").nth(priceValue)).to_have_text("37")
    print("✅ Successfully verified the price of Rice")