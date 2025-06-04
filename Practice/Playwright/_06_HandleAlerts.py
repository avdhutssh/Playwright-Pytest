"""
Handle Different Types of Alerts - Playwright Python
Website: https://the-internet.herokuapp.com/javascript_alerts
"""

from playwright.sync_api import sync_playwright, Page


def test_simple_alert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    def handle_dialog(dialog):
        print(f"Alert text: {dialog.message}")
        assert dialog.message == "I am a JS Alert"
        dialog.accept()
    
    page.on("dialog", handle_dialog)
    
    page.click("text=Click for JS Alert")
    
    result = page.locator("#result").text_content()
    assert "You successfully clicked an alert" in result
    print(f"✅ Simple Alert: {result}")
    
    

def test_confirmation_alert_ok(page:Page):
    """Test confirmation alert - OK button"""

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    def handle_dialog(dialog):
        print(f"Confirm text: {dialog.message}")
        assert dialog.message == "I am a JS Confirm"
        dialog.accept()
    
    page.on("dialog", handle_dialog)
    
    page.click("text=Click for JS Confirm")
    
    result = page.locator("#result").text_content()
    assert "You clicked: Ok" in result
    print(f"✅ Confirmation OK: {result}")
    
    

def test_confirmation_alert_cancel(page:Page):
    """Test confirmation alert - Cancel button"""

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    def handle_dialog(dialog):
        print(f"Confirm text: {dialog.message}")
        assert dialog.message == "I am a JS Confirm"
        dialog.dismiss()
    
    page.on("dialog", handle_dialog)
    
    page.click("text=Click for JS Confirm")
    
    result = page.locator("#result").text_content()
    assert "You clicked: Cancel" in result
    print(f"✅ Confirmation Cancel: {result}")

def test_prompt_alert_enter_text(page:Page):
    """Test prompt alert - Enter text"""

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    def handle_dialog(dialog):
        print(f"Prompt text: {dialog.message}")
        dialog.accept("Hello Avdhut")
    
    page.on("dialog", handle_dialog)
    
    page.click("text=Click for JS Prompt")
    
    result = page.locator("#result").text_content()
    assert "You entered: Hello Avdhut" in result
    print(f"✅ Prompt with text: {result}")

def test_prompt_alert_ok_empty(page:Page):
    """Test prompt alert - Click OK with empty text"""

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    def handle_dialog(dialog):
        print(f"Prompt text: {dialog.message}")
        dialog.accept("")
    
    page.on("dialog", handle_dialog)
    page.click("text=Click for JS Prompt")
    
    result = page.locator("#result").text_content()
    assert "You entered:" in result
    print(f"✅ Prompt empty: {result}")

def test_prompt_alert_cancel(page:Page):
    """Test prompt alert - Click Cancel"""

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    def handle_dialog(dialog):
        print(f"Prompt text: {dialog.message}")
        dialog.dismiss()
    
    page.on("dialog", handle_dialog)
    
    page.click("text=Click for JS Prompt")
    
    result = page.locator("#result").text_content()
    assert "You entered: null" in result
    print(f"✅ Prompt cancel: {result}")