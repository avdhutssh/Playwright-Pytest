"""
SauceDemo E-commerce Test - Login, Add Products, Verify Cart
Website: https://www.saucedemo.com/
"""

from playwright.sync_api import sync_playwright, Page
import time

def test_saucedemo_cart_functionality(page:Page):
    """
    Test case for SauceDemo:
    1. Login to the website
    2. Add two specific products to cart
    3. Verify cart count and product names
    """
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]
    
    print("🛒 SauceDemo Cart Test")
    print("=" * 50)
    print(f"📝 Products to add: {products_to_add}")
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    assert page.url == "https://www.saucedemo.com/inventory.html"
    print("✅ Login successful!")
    for product_name in products_to_add:
        product_locator = page.locator(".inventory_item").filter(has_text=product_name)
        add_to_cart_btn = product_locator.locator("button", has_text="Add to cart")
        add_to_cart_btn.click()
        print(f"✅ Added '{product_name}' to cart")

    cart_badge = page.locator(".shopping_cart_badge")
    cart_count = cart_badge.text_content()

    expected_count = str(len(products_to_add))
    assert cart_count == expected_count, f"Expected {expected_count} items, but got {cart_count}"
    print(f"✅ Cart badge shows correct count: {cart_count}")
    page.locator(".shopping_cart_link").click()
    assert "cart.html" in page.url
    print("✅ Successfully navigated to cart page")

    cart_items = page.locator(".cart_item")
    actual_cart_count = cart_items.count()

    assert actual_cart_count == len(products_to_add), f"Expected {len(products_to_add)} items in cart, but found {actual_cart_count}"
    print(f"✅ Cart contains correct number of items: {actual_cart_count}")

    for i in range(actual_cart_count):
        cart_item = cart_items.nth(i)
        product_name = cart_item.locator(".inventory_item_name").text_content()
        assert product_name in products_to_add, f"Product '{product_name}' not found in cart"
        print(f"   🔹 Found in cart: '{product_name}'")
    print(f"✅ Verified Added Products in cart")

    for i, expected_product in enumerate(products_to_add):
        cart_item = cart_items.nth(i)

        product_name = cart_item.locator(".inventory_item_name").text_content()
        product_desc = cart_item.locator(".inventory_item_desc").text_content()
        product_price = cart_item.locator(".inventory_item_price").text_content()

        print(f"   📦 Product {i+1}:")
        print(f"      Name: {product_name}")
        print(f"      Description: {product_desc}")
        print(f"      Price: {product_price}")