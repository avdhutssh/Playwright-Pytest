from playwright.sync_api import expect

from EcomAppAutomationFramework.PageObjects.orderDetailsPage import orderDetailsPage


class ordersPage:
    def __init__(self,page):
        self.page = page
        self.delete_buttons = page.locator("button.btn-danger")
        self.no_orders_text = page.get_by_text("You have No Orders to show at")


    def delete_all_existing_orders(self):
        delete_count = self.delete_buttons.count()
        print(f"Number of delete buttons found: {delete_count}")
        while self.delete_buttons.count() > 0:
            self.delete_buttons.first.click()
            self.page.wait_for_timeout(1000)
        print("✅ All existing orders deleted")

    def verify_no_orders_present(self):
        expect(self.no_orders_text).to_be_visible()
        return True

    def verify_order_present(self, orderID):
        expect(self.page.get_by_text(orderID)).to_be_visible()
        print(f"✅ Order with ID: {orderID} is present")
        return True

    def click_view_button_for_order(self, order_id):
        order_row = self.page.locator("tr").filter(has_text=order_id)
        order_row.get_by_role("button", name="View").click()
        return orderDetailsPage(self.page)
