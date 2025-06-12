from playwright.sync_api import expect
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

class checkoutPage:
    def __init__(self, page):
        self.page = page
        self.country_input = page.locator("[placeholder*='Country']")
        self.country_dropdown = page.locator(".ta-results")
        self.place_order_button = page.locator(".action__submit")
        self.card_number_input = page.locator("(//input[@type='text'])[1]")
        self.cvv_input = page.locator("(//input[@type='text'])[2]")
        self.name_on_card_input = page.locator("(//input[@type='text'])[3]")
        
    def enter_shipping_country(self, country_name):
        logger.info(f"Entering shipping country: {country_name}")
        for char in country_name:
            self.country_input.type(char)
            self.page.wait_for_timeout(200)
        self.page.locator(f"//span[normalize-space(text())='{country_name}']").click()
        logger.info(f"Selected country: {country_name}")
        
    def enter_payment_info(self, card_number="4242424242424242", name_on_card="Test User", expiry_date="12/25", cvv="123"):
        logger.info("Entering payment information")
        self.card_number_input.fill(card_number)
        self.name_on_card_input.fill(name_on_card)
        self.cvv_input.fill(cvv)
        logger.info("Payment information entered")
        
    def place_order(self):
        logger.info("Placing order")
        self.place_order_button.click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Order placed successfully")
        # Import here to avoid circular imports
        from EcomAppAutomationFramework.PageObjects.orderDetailsPage import orderDetailsPage
        return orderDetailsPage(self.page) 