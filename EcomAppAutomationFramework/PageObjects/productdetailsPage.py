from playwright.sync_api import expect


class productDetailsPage:
    def __init__(self,page):
        self.page = page

    def get_current_product_id(self):
        product_url = self.page.url
        print(f"✅ Product URL: {product_url}")
        product_id = product_url.split("/")[-1]
        print(f"✅ Product ID extracted: {product_id}")
        return product_id

    def verify_product_is_visible(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()
        return True