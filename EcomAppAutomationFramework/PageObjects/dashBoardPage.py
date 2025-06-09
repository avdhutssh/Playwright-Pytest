import time
from playwright.sync_api import expect

from EcomAppAutomationFramework.PageObjects.ordersPage import ordersPage
from EcomAppAutomationFramework.PageObjects.productdetailsPage import productDetailsPage


class dashboardPage:
    def __init__(self, page):
        self.page = page
        self.orders_button = page.get_by_role("button", name="ORDERS")

    def click_product_view(self, product_name):
        view_button = self.page.locator(f"//*[normalize-space(text())='{product_name}']/../..//button[normalize-space(text())='View']")
        view_button.click()
        return productDetailsPage(self.page)

    def navigate_to_orders(self):
        self.orders_button.click()
        time.sleep(2)
        return ordersPage(self.page)
