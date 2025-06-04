"""
Window Switching Test - Rahul Shetty Academy
Website: https://rahulshettyacademy.com/loginpagePractise/
"""

from playwright.sync_api import sync_playwright, Playwright
import time

def test_window_switching(playwright: Playwright):
    """
    Test case for window switching:
    1. Open main page
    2. Click link that opens new window
    3. Switch to new window and extract data
    4. Switch back to original window
    """
    
    print("🔄 Window Switching Test")
    print("=" * 50)
    
    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_context()
    page1 = context.new_page()
    
    page1.goto("https://rahulshettyacademy.com/loginpagePractise/")
    time.sleep(2)
    
    window1_title = page1.title()
    print(f"📄 Window 1 Title: {window1_title}")
    
    with context.expect_page() as new_page_info:
        page1.click("text=Free Access to InterviewQues/ResumeAssistance/Material")
    
    page2 = new_page_info.value
    page2.wait_for_load_state()
    time.sleep(2)
    
    window2_title = page2.title()
    print(f"📄 Window 2 Title: {window2_title}")
    
    red_elements = page2.locator(".red").text_content();
    print(red_elements)
    actualEmail = "mentor@rahulshettyacademy.com"
    extracted_email = red_elements.split("at")[1].strip().split(" ")[0]
    assert actualEmail in extracted_email, f"Expected {actualEmail} but found {extracted_email}"

    page2.close()
    page1.bring_to_front()
    time.sleep(1)
    
    current_title = page1.title()
    print(f"📄 Back to Window 1 Title: {current_title}")
    assert current_title == window1_title, "Failed to switch back to original window"
    browser.close()