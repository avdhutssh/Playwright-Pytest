import pytest
from playwright.sync_api import Playwright

baseURL = "https://rahulshettyacademy.com"
ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}

class API_Factory:
    @staticmethod
    def get_headers(playwright: Playwright,user_credentials):  # Removed 'self' since this is static
        token = API_Factory.getToken(playwright,user_credentials)  # Use class name to call method
        print("token is: ", token)
        return {
            "Authorization": token,
            "Accept": "application/json"
        }

    @staticmethod
    def getToken(playwright: Playwright,user_credentials):
        user_email = user_credentials['userEmail']
        user_Password = user_credentials['userPassword']
        apiRequestContext = playwright.request.new_context(base_url=baseURL)
        response = apiRequestContext.post("/api/ecom/auth/login",
                                         data={"userEmail":user_email,"userPassword":user_Password})
        assert response.ok, f"Failed to get token: {response.status} {response.text}"
        response_json = response.json()
        print(response_json)
        return response_json["token"]

    def createOrder(self, playwright: Playwright, productId, user_credentials):
        apiRequestContext = playwright.request.new_context(base_url=baseURL)
        response = apiRequestContext.post("/api/ecom/order/create-order",
                                            data={"orders": [{"country": "India", "productOrderedId": productId}]},
                                            headers=self.get_headers(playwright,user_credentials))

        assert response.status == 201, f"Failed to create order: {response.status} {response.text}"
        assert response.status_text == "Created", f"Expected status text 'Created' but got {response.status_text}"
        response_body = response.json()
        print(response_body)
        orderId = response_body["orders"][0]
        return orderId