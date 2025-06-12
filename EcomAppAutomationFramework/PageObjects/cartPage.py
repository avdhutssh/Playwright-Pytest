from playwright.sync_api import expect
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

class cartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cartSection h3")
        self.checkout_button = page.locator("//button[contains(text(), 'Checkout')]")
        self.product_in_cart = lambda product_name: page.locator(f"//h3[contains(text(), '{product_name}')]")
        self.remove_button = lambda product_name: page.locator(f"//h3[contains(text(), '{product_name}')]/parent::div/parent::div//button[@class='btn btn-danger']")
        self.empty_message = page.locator("(//h1)[2]")

    def navigate_to_cart(self):
        logger.info("Navigating to cart page")
        self.page.locator("[routerlink*='cart']").click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Navigated to cart page")
        
    def verify_product_in_cart(self, product_name):
        logger.info(f"Verifying product {product_name} is in cart")
        product = self.product_in_cart(product_name)
        expect(product).to_be_visible()
        logger.info(f"Product {product_name} is in cart")
        return True
    
    def remove_product_from_cart(self, product_name):
        logger.info(f"Removing product {product_name} from cart")
        remove_button = self.remove_button(product_name)
        expect(remove_button).to_be_visible()
        remove_button.click()
        logger.info(f"Product {product_name} removed from cart")

    def is_cart_empty(self):
        logger.info("Checking if cart is empty")
        try:
            expect(self.empty_message).to_have_text("No Products in Your Cart !")
            logger.info("Cart is empty")
            return True
        except:
            logger.info("Cart is not empty")
            return False
            
    def proceed_to_checkout(self):
        logger.info("Proceeding to checkout")
        expect(self.checkout_button).to_be_visible()
        self.checkout_button.click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Navigated to checkout page")
        from EcomAppAutomationFramework.PageObjects.checkoutPage import checkoutPage
        return checkoutPage(self.page) 