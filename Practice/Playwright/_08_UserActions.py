"""
User Actions Automation - Playwright Python
"""

from playwright.sync_api import sync_playwright, Page, expect
import time
import tempfile
import os

def test_click_action(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.click("button:has-text('Add Element')")
    assert page.locator(".added-manually").count() == 1
    print("✅ Click action completed")

def test_type_action(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    assert page.locator("#username").input_value() == "tomsmith"
    print("✅ Type action completed")

def test_double_click_action(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.dblclick("text=A/B Testing")
    print("✅ Double click action completed")

def test_right_click_action(page: Page):
    page.goto("https://the-internet.herokuapp.com/context_menu")
    page.click("#hot-spot", button="right")
    page.on("dialog", lambda dialog: dialog.accept())
    print("✅ Right click action completed")

def test_enter_key_action(page: Page):
    page.goto("https://the-internet.herokuapp.com/key_presses")
    page.locator("#target").press("Tab")
    result = page.locator("#result").text_content()
    assert "TAB" in result
    print("✅ Enter key action completed")

def test_dropdown_select_by_value(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("#dropdown", value="1")
    assert page.locator("#dropdown").input_value() == "1"
    print("✅ Dropdown select by value completed")

def test_dropdown_select_by_text(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("#dropdown", label="Option 2")
    assert page.locator("#dropdown").input_value() == "2"
    print("✅ Dropdown select by text completed")

def test_dropdown_select_by_index(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("#dropdown", index=1)
    assert page.locator("#dropdown").input_value() == "1"
    print("✅ Dropdown select by index completed")

def test_checkbox_check_uncheck(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox = page.locator("input[type='checkbox']").first
    checkbox.check()
    assert checkbox.is_checked()
    checkbox.uncheck()
    assert not checkbox.is_checked()
    print("✅ Checkbox check/uncheck completed")

def test_radio_button_selection(page: Page):
    page.goto("https://demo.guru99.com/test/radio.html")
    page.check("input[value='Option 1']")
    assert page.is_checked("input[value='Option 1']")
    print("✅ Radio button selection completed")

def test_scroll_into_view(page: Page):
    page.goto("https://the-internet.herokuapp.com/infinite_scroll")
    page.locator("text=Eius").scroll_into_view_if_needed()
    print("✅ Scroll into view completed")

def test_scroll_by_pixels(page: Page):
    page.goto("https://the-internet.herokuapp.com/infinite_scroll")
    page.mouse.wheel(0, 500)
    time.sleep(1)
    print("✅ Scroll by pixels completed")

def test_hover_action(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.hover(".figure img")
    assert page.locator(".figcaption").first.is_visible()
    print("✅ Hover action completed")

def test_drag_and_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    page.drag_and_drop("#column-a", "#column-b")
    assert page.locator("#column-a header").text_content() == "B"
    print("✅ Drag and drop completed")

def test_file_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
        temp_file.write("This is a test file for upload")
        temp_file_path = temp_file.name
    
    try:
        page.set_input_files("#file-upload", temp_file_path)
        page.click("#file-submit")
        assert "File Uploaded!" in page.locator("h3").text_content()
        print("✅ File upload completed")
    finally:
        os.unlink(temp_file_path)

def test_tab_navigation(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.focus("#username")
    page.keyboard.press("Tab")
    is_focused = page.locator("#password").evaluate("element => element === document.activeElement")
    assert is_focused
    print("✅ Tab navigation completed")

def test_keyboard_shortcuts(page: Page):
    page.goto("https://the-internet.herokuapp.com/key_presses")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    print("✅ Keyboard shortcuts completed")

def test_clear_input(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "test")
    page.locator("#username").clear()
    assert page.locator("#username").input_value() == ""
    print("✅ Clear input completed")

def test_get_text_content(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    title = page.locator("h1").text_content()
    assert "Welcome to the-internet" in title
    print(f"✅ Text content: {title}")

def test_get_attribute_value(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    id_attr = page.locator("#username").get_attribute("id")
    assert id_attr == "username"
    print(f"✅ Attribute value: {id_attr}")

def test_wait_for_element(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.click("button:has-text('Start')")
    page.wait_for_selector("text=Hello World!", timeout=10000)
    assert page.locator("text=Hello World!").is_visible()
    print("✅ Wait for element completed")

def test_multiple_selection_dropdown(page: Page):
    page.goto("https://demo.guru99.com/test/newtours/reservation.php")
    page.select_option("select[name='passCount']", ["2"])
    print("✅ Multiple selection dropdown completed")
