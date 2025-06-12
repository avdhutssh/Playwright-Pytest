from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from playwright.sync_api import expect
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

class loginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("email@example.com")
        self.password_input = page.locator("#userPassword")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_error = page.locator(".toast-message, .alert-danger, .ng-star-inserted")
        self.login_page_elements = page.locator(".login-title")

    def navigate_to_login(self):
        logger.info("Navigating to login page")
        self.page.goto("https://rahulshettyacademy.com/client")

    def loginToApp(self, username, password):
        logger.info(f"Attempting to login with username: {username}")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return dashboardPage(self.page)
    
    def is_login_error_displayed(self):
        logger.info("Checking for login error message")
        self.page.wait_for_timeout(1000)
        error_visible = self.login_error.is_visible()
        if not error_visible:
            error_visible = self.login_page_elements.is_visible()
        
        logger.info(f"Login error displayed: {error_visible}")
        return error_visible
    
    def is_login_page_displayed(self):
        logger.info("Checking if login page is displayed")
        return self.login_button.is_visible()