from playwright.sync_api import expect

class orderDetailsPage:
    def __init__(self, page):
        self.page = page
        self.tagline_locator = page.locator(".tagline")
        self.order_table = page.locator("table")

    def verify_thank_you_message(self):
        expect(self.tagline_locator).to_contain_text("Thank you for Shopping With Us")
        print("✅ Order details page is displayed")
        return True