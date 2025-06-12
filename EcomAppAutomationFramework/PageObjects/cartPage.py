from playwright.sync_api import expect
import allure
from EcomAppAutomationFramework.Common_Utils.logger import get_logger
from EcomAppAutomationFramework.Common_Utils.allure_utils import attach_screenshot

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
        with allure.step("Navigating to cart page"):
            logger.info("Navigating to cart page")
            attach_screenshot(self.page, "Before navigating to cart")
            self.page.locator("[routerlink*='cart']").click()
            self.page.wait_for_load_state("networkidle")
            attach_screenshot(self.page, "After navigating to cart")
            logger.info("Navigated to cart page")
        
    def verify_product_in_cart(self, product_name):
        with allure.step(f"Verifying product {product_name} is in cart"):
            logger.info(f"Verifying product {product_name} is in cart")
            attach_screenshot(self.page, f"Checking for {product_name} in cart")
            product = self.product_in_cart(product_name)
            is_visible = product.is_visible()
            
            if is_visible:
                allure.attach(
                    self.page.screenshot(),
                    name=f"Product {product_name} found in cart",
                    attachment_type=allure.attachment_type.PNG
                )
                logger.info(f"Product {product_name} is in cart")
            else:
                allure.attach(
                    self.page.screenshot(),
                    name=f"Product {product_name} NOT found in cart",
                    attachment_type=allure.attachment_type.PNG
                )
                logger.info(f"Product {product_name} is NOT in cart")
                
            return is_visible
    
    def remove_product_from_cart(self, product_name):
        with allure.step(f"Removing product {product_name} from cart"):
            logger.info(f"Removing product {product_name} from cart")
            attach_screenshot(self.page, f"Before removing {product_name} from cart")
            remove_button = self.remove_button(product_name)
            expect(remove_button).to_be_visible()
            remove_button.click()
            self.page.wait_for_load_state("networkidle")
            attach_screenshot(self.page, f"After removing {product_name} from cart")
            logger.info(f"Product {product_name} removed from cart")

    def is_cart_empty(self):
        with allure.step("Checking if cart is empty"):
            logger.info("Checking if cart is empty")
            attach_screenshot(self.page, "Checking if cart is empty")
            try:
                expect(self.empty_message).to_have_text("No Products in Your Cart !")
                attach_screenshot(self.page, "Cart is empty")
                logger.info("Cart is empty")
                return True
            except:
                attach_screenshot(self.page, "Cart is not empty")
                logger.info("Cart is not empty")
                return False
            
    def proceed_to_checkout(self):
        with allure.step("Proceeding to checkout"):
            logger.info("Proceeding to checkout")
            attach_screenshot(self.page, "Before proceeding to checkout")
            expect(self.checkout_button).to_be_visible()
            self.checkout_button.click()
            self.page.wait_for_load_state("networkidle")
            attach_screenshot(self.page, "After proceeding to checkout")
            logger.info("Navigated to checkout page")
            from EcomAppAutomationFramework.PageObjects.checkoutPage import checkoutPage
            return checkoutPage(self.page) 