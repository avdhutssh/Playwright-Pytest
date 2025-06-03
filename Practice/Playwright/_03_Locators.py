"""
Simple Locators Guide - One Example Each
Practice Website: https://the-internet.herokuapp.com/
"""

from playwright.sync_api import sync_playwright
import pytest_check as check
import time

def test_all_locators():
    """Test all locator types with one example each"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        page = browser.new_page()
        
        print("🎯 Testing All Locator Types")
        
        # 1. get_by_text
        page.goto("https://the-internet.herokuapp.com/")
        page.get_by_text("Checkboxes").click()
        print("✅ get_by_text: Clicked Checkboxes link")
        time.sleep(1)
        
        # 2. CSS selector
        checkbox = page.locator("input[type='checkbox']").first
        checkbox.uncheck()
        assert not checkbox.is_checked(), "Checkbox should not be checked"
        checkbox.check()
        print("✅ CSS selector: Checked first checkbox")
        assert checkbox.is_checked(), "Checkbox should be checked"
        time.sleep(1)
        
        # 3. XPath
        page.goto("https://the-internet.herokuapp.com/dropdown")
        dropdown = page.locator("//select[@id='dropdown']")
        dropdown.select_option("1")

        check.equal(dropdown.input_value(), "1", "Dropdown should have option 1 selected")
        print("✅ XPath: Selected dropdown option")
        time.sleep(1)
        
        # 4. ID selector
        page.goto("https://the-internet.herokuapp.com/login")
        page.locator("#username").fill("tomsmith")
        print("✅ ID selector: Filled username")
        time.sleep(1)
        
        # 5. get_by_label
        page.get_by_label("Password").fill("SuperSecretPassword!")
        print("✅ get_by_label: Filled number input")
        time.sleep(1)
        
        # 6. get_by_role
        page.get_by_role("button", name="Login").click()
        print("✅ get_by_role: Clicked login button")
        time.sleep(2)

        # # 7. get_by_test_id
        # page.goto("https://demo.playwright.dev/todomvc/")
        # page.get_by_test_id("todo-input").fill("Learn Playwright")
        # page.get_by_test_id("todo-input").press("Enter")
        # print("✅ get_by_test_id: Added a todo item")
        # time.sleep(1)
        #
        # # 8. get_by_alt
        # page.goto("https://the-internet.herokuapp.com/")
        # page.get_by_alt("Elemental Selenium").click()
        # print("✅ get_by_alt: Clicked Elemental Selenium link")
        # time.sleep(1)

