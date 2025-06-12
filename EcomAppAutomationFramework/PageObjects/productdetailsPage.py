from playwright.sync_api import expect
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

class productDetailsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add To Cart")

    def get_current_product_id(self):
        product_url = self.page.url
        logger.info(f"Product URL: {product_url}")
        product_id = product_url.split("/")[-1]
        logger.info(f"Product ID extracted: {product_id}")
        return product_id

    def verify_product_is_visible(self, product_name):
        logger.info(f"Verifying product '{product_name}' is visible")
        expect(self.page.get_by_text(product_name)).to_be_visible()
        return True
        
    def add_to_cart(self):
        logger.info("Adding product to cart from details page")
        self.add_to_cart_button.click()
        logger.info("Product added to cart from details page")