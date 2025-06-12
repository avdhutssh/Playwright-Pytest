from playwright.sync_api import expect
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

class orderDetailsPage:
    def __init__(self, page):
        self.page = page
        self.tagline_locator = page.locator(".tagline")
        self.successMsg = page.locator(".hero-primary")
        self.order_id = page.locator(".em-spacer-1 .ng-star-inserted")
        self.order_details_table = page.locator("table.table")
        self.download_order_button = page.get_by_text("Click To Download Order Details in CSV")

    def verify_thank_you_message(self):
        logger.info("Verifying thank you message is displayed")
        logger.info(self.tagline_locator.text_content())
        expect(self.tagline_locator).to_contain_text("Thank you for Shopping With Us")
        logger.info("Order confirmation message verified")
        return True

    def verify_successful_order_msg(self):
        logger.info("Verifying Thankyou for the order message is displayed")
        expect(self.successMsg).to_contain_text("Thankyou for the order")
        logger.info("Order confirmation message verified")
        return True

    def get_order_id(self):
        logger.info("Getting order ID")
        order_id_text = self.order_id.text_content()
        order_id = order_id_text.split(" | ")[0].strip()
        logger.info(f"Order ID: {order_id}")
        return order_id
        
    def verify_order_details_table(self):
        logger.info("Verifying order details table is displayed")
        expect(self.order_details_table).to_be_visible()
        logger.info("Order details table is displayed")
        return True
        
    def download_order_details(self):
        logger.info("Downloading order details")
        with self.page.expect_download() as download_info:
            self.download_order_button.click()
        download = download_info.value
        logger.info(f"Order details downloaded as {download.suggested_filename}")
        return download.suggested_filename