import time
from playwright.sync_api import expect
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

from EcomAppAutomationFramework.PageObjects.ordersPage import ordersPage
from EcomAppAutomationFramework.PageObjects.productdetailsPage import productDetailsPage
from EcomAppAutomationFramework.PageObjects.cartPage import cartPage

logger = get_logger(__name__)

class dashboardPage:
    def __init__(self, page):
        self.page = page
        self.orders_button = page.get_by_role("button", name="ORDERS")
        self.search_input = page.locator("(//input[@name='search'])[2]")
        self.cart_button = page.locator("[routerlink*='cart']")
        self.toast_message = page.locator(".toast-container")

    def click_product_view(self, product_name):
        logger.info(f"Clicking view button for product: {product_name}")
        view_button = self.page.locator(f"//*[normalize-space(text())='{product_name}']/../..//button[normalize-space(text())='View']")
        view_button.click()
        return productDetailsPage(self.page)

    def navigate_to_orders(self):
        logger.info("Navigating to orders page")
        self.orders_button.click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Navigated to orders page")
        return ordersPage(self.page)
    
    def search_product(self, product_name):
        logger.info(f"Searching for product: {product_name}")
        self.search_input.fill(product_name)
        self.page.keyboard.press("Enter")
      
    def is_product_search_result_displayed(self, product_name):
        logger.info(f"Checking if search result for '{product_name}' is displayed")
        self.page.wait_for_load_state("networkidle")
        return self.page.locator(f"//*[contains(text(),'{product_name}')]").is_visible(timeout=5000)

    def add_product_to_cart(self, product_name):
        logger.info(f"Adding product {product_name} to cart")
        self.page.wait_for_load_state("networkidle")
        self.page.locator(f"//*[normalize-space(text())='{product_name}']/../..//*[normalize-space(text())='Add To Cart']").click()
        self.toast_message.wait_for(state="visible")
        logger.info(f"Product {product_name} added to cart successfully")
        
    def navigate_to_cart(self):
        logger.info("Navigating to cart page")
        self.cart_button.click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Navigated to cart page")
        return cartPage(self.page)

    def verify_product_visible(self, product_name):
        logger.info(f"Verifying product {product_name} is visible")
        product_card = self.page.locator(f"//h5[contains(text(),'{product_name}')]/ancestor::div[contains(@class, 'card')]")
        expect(product_card).to_be_visible()
        logger.info(f"Product {product_name} is visible")
        return True
        
    def navigate_to_product_details(self, product_name):
        logger.info(f"Navigating to product details for {product_name}")
        product_card = self.page.locator(f"//h5[contains(text(),'{product_name}')]/ancestor::div[contains(@class, 'card')]")
        product_title = product_card.locator("h5")
        product_title.click()
        self.page.wait_for_load_state("networkidle")
        logger.info(f"Navigated to product details for {product_name}")
        return productDetailsPage(self.page)
