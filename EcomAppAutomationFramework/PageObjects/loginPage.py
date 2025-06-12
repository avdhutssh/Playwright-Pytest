from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from playwright.sync_api import expect
import allure
from EcomAppAutomationFramework.Common_Utils.logger import get_logger
from EcomAppAutomationFramework.Common_Utils.allure_utils import attach_screenshot

logger = get_logger(__name__)

class loginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("email@example.com")
        self.password_input = page.locator("#userPassword")
        self.login_button = page.get_by_role("button", name="Login")
        # Error messages can appear in toast notifications or alerts
        self.login_error = page.locator(".toast-message, .alert-danger, .ng-star-inserted")
        self.login_page_elements = page.locator(".login-title")

    def navigate_to_login(self):
        with allure.step("Navigating to login page"):
            logger.info("Navigating to login page")
            self.page.goto("https://rahulshettyacademy.com/client")
            attach_screenshot(self.page, "Login page")

    def loginToApp(self, username, password):
        with allure.step(f"Logging in with username: {username}"):
            logger.info(f"Attempting to login with username: {username}")
            attach_screenshot(self.page, "Before login")
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()
            self.page.wait_for_load_state("networkidle")
            attach_screenshot(self.page, "After login")
            return dashboardPage(self.page)
    
    def is_login_error_displayed(self):
        with allure.step("Checking for login error message"):
            logger.info("Checking for login error message")
            # Wait a bit for any toast notifications to appear
            self.page.wait_for_timeout(1000)
            attach_screenshot(self.page, "Checking for login error")
            
            # Check for toast notifications or error messages
            error_visible = self.login_error.is_visible()
            if not error_visible:
                # If no explicit error, check if we're still on login page (implicit error)
                error_visible = self.login_page_elements.is_visible()
            
            if error_visible:
                allure.attach(
                    self.page.screenshot(),
                    name="Login error displayed",
                    attachment_type=allure.attachment_type.PNG
                )
            else:
                allure.attach(
                    self.page.screenshot(),
                    name="No login error displayed",
                    attachment_type=allure.attachment_type.PNG
                )
                
            logger.info(f"Login error displayed: {error_visible}")
            return error_visible
    
    def is_login_page_displayed(self):
        with allure.step("Checking if login page is displayed"):
            logger.info("Checking if login page is displayed")
            attach_screenshot(self.page, "Checking if on login page")
            is_displayed = self.login_button.is_visible()
            
            if is_displayed:
                allure.attach(
                    self.page.screenshot(),
                    name="Login page is displayed",
                    attachment_type=allure.attachment_type.PNG
                )
            else:
                allure.attach(
                    self.page.screenshot(),
                    name="Login page is not displayed",
                    attachment_type=allure.attachment_type.PNG
                )
                
            return is_displayed