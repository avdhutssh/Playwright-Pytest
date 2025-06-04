"""
Window Switching Test - Rahul Shetty Academy
Website: https://rahulshettyacademy.com/loginpagePractise/
"""

from playwright.sync_api import sync_playwright, Playwright, BrowserContext
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
    
    red_elements = page2.locator(".red").text_content()
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


#Utility function to switch to a window by number
def switch_to_window(context: BrowserContext, window_number: int):
    """
    Switch to window by number (1-based index)
    Args:
        context: Browser context containing all pages
        window_number: Window number to switch to (1, 2, 3, etc.)
    """
    pages = context.pages
    total_windows = len(pages)

    if window_number > total_windows:
        raise RuntimeError(
            f"The specified window number ({window_number}) is greater than the number of windows created ({total_windows}).")

    target_page = pages[window_number - 1]
    target_page.bring_to_front()
    print(f"✅ Successfully switched to window number: {window_number}")
    return target_page


def test_window_switching_by_numbers(playwright: Playwright):
    """
    Test window switching using window numbers (1, 2, 3, etc.)
    """
    
    print("🔢 Window Switching by Numbers Test")
    print("=" * 50)
    
    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_context()
    
    page1 = context.new_page()
    page1.goto("https://rahulshettyacademy.com/loginpagePractise/")
    time.sleep(2)
    
    print(f"📊 Total windows: {len(context.pages)}")
    
    current_page = switch_to_window(context, 1)
    window1_title = current_page.title()
    print(f"📄 Window 1 Title: {window1_title}")
    
    with context.expect_page() as new_page_info:
        current_page.click("text=Free Access to InterviewQues/ResumeAssistance/Material")
    
    page2 = new_page_info.value
    page2.wait_for_load_state()
    time.sleep(2)
    
    print(f"📊 Total windows: {len(context.pages)}")
    
    current_page = switch_to_window(context, 2)
    window2_title = current_page.title()
    print(f"📄 Window 2 Title: {window2_title}")
    
    red_elements = current_page.locator(".red").text_content()
    actualEmail = "mentor@rahulshettyacademy.com"
    extracted_email = red_elements.split("at")[1].strip().split(" ")[0]
    assert actualEmail in extracted_email, f"Expected {actualEmail} but found {extracted_email}"
    print(f"📧 Extracted email: {extracted_email}")
    
    current_page = switch_to_window(context, 1)
    back_title = current_page.title()
    print(f"📄 Back to Window 1 Title: {back_title}")
    assert back_title == window1_title, "Failed to switch back to original window"
    
    browser.close()