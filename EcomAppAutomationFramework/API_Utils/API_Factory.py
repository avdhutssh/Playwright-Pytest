import pytest
from playwright.sync_api import Playwright

baseURL = "https://rahulshettyacademy.com"
ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}

class API_Factory:
    @staticmethod
    def get_headers(playwright: Playwright):  # Removed 'self' since this is static
        token = API_Factory.getToken(playwright)  # Use class name to call method
        print("token is: ", token)
        return {
            "Authorization": token,
            "Accept": "application/json"
        }

    @staticmethod
    def getToken(playwright: Playwright):
        apiRequestContext = playwright.request.new_context(base_url=baseURL)
        response = apiRequestContext.post("/api/ecom/auth/login",
                                         data={"userEmail":"av1234@gmail.com","userPassword":"Bulbul@123"})
        assert response.ok, f"Failed to get token: {response.status} {response.text}"
        response_json = response.json()
        print(response_json)
        return response_json["token"]

    def createOrder(self, playwright: Playwright, productId: str = "67a8df56c0d3e6622a297ccd"):
        apiRequestContext = playwright.request.new_context(base_url=baseURL)
        response = apiRequestContext.post("/api/ecom/order/create-order",
                                            data={"orders": [{"country": "India", "productOrderedId": productId}]},
                                            headers=self.get_headers(playwright))

        assert response.status == 201, f"Failed to create order: {response.status} {response.text}"
        assert response.status_text == "Created", f"Expected status text 'Created' but got {response.status_text}"
        response_body = response.json()
        print(response_body)
        orderId = response_body["orders"][0]
        return orderId

# Add a proper pytest test function at the module level
@pytest.fixture(scope="module")
def API_Factory():
    return API_Factory()

def test_create_order(playwright: Playwright, API_Factory):
    print("🔄 Create Order Test")
    print("=" * 50)
    orderId = API_Factory.createOrder(playwright)
    print(f"✅ Order created successfully with ID: {orderId}")
    assert orderId is not None