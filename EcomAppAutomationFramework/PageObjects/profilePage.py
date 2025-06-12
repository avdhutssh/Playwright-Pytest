from playwright.sync_api import expect
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

class profilePage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.profile_button = page.locator("button.btn-custom")
        self.name_input = page.locator("#firstName, [formcontrolname='firstName']")
        self.phone_input = page.locator("input[type='tel'], [formcontrolname='mobileNumber']")
        self.save_button = page.locator("input[type='submit'], button:has-text('Save')")
        self.logout_button = page.get_by_text("Sign Out")
        self.update_success_message = page.locator(".toast-success, .alert-success")

    def navigate_to_profile(self):
        logger.info("Navigating to profile page")
        # Find the dropdown with the user profile and click it
        self.page.locator(".fa-user-circle").first.click()
        self.page.get_by_text("My Profile").click()
        self.page.wait_for_selector("form")
        logger.info("Profile page loaded")

    def update_profile_info(self, name=None, phone=None):
        logger.info("Updating profile information")
        self.navigate_to_profile()
        
        if name:
            logger.info(f"Updating name to: {name}")
            self.name_input.fill(name)
        
        if phone:
            logger.info(f"Updating phone to: {phone}")
            self.phone_input.fill(phone)
        
        self.save_button.click()
        logger.info("Profile information saved")
        # Wait for toast notifications
        self.page.wait_for_timeout(1000)

    def is_profile_update_successful(self):
        logger.info("Checking for profile update success message")
        return self.update_success_message.is_visible() or self.page.get_by_text("Profile Updated Successfully").is_visible()

    def logout(self):
        logger.info("Logging out of the application")
        self.page.locator(".fa-user-circle").first.click()
        self.logout_button.click()
        logger.info("Clicked logout button")
        # Wait for redirect
        self.page.wait_for_timeout(1000) 