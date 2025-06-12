from playwright.sync_api import Playwright, APIRequestContext
import json
import allure
from EcomAppAutomationFramework.Common_Utils.logger import get_logger
from EcomAppAutomationFramework.Common_Utils.allure_utils import attach_api_request, attach_api_response

logger = get_logger(__name__)

class API_Client:
    """
    Generic API client with all HTTP methods and logging capabilities
    """
    def __init__(self, playwright: Playwright, base_url="https://rahulshettyacademy.com"):
        """
        Initialize API client with Playwright context
        """
        self.base_url = base_url
        self.api_context = playwright.request.new_context(base_url=base_url)
        self.default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        logger.info(f"API Client initialized with base URL: {base_url}")

    def set_authorization(self, token):
        """
        Set authorization token for API requests
        """
        self.default_headers["Authorization"] = token
        logger.info("Authorization token set")

    def get_headers(self, additional_headers=None):
        """
        Get headers for API requests
        """
        headers = self.default_headers.copy()
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def format_response_log(self, response):
        """
        Format response log message
        """
        try:
            response_json = response.json()
            response_body = json.dumps(response_json, indent=2)
        except:
            response_body = response.text()
        
        # Get headers as dictionary - headers property is not callable
        headers_dict = dict(response.headers)
        
        return (f"Response Status: {response.status} {response.status_text}\n"
                f"Response Headers: {json.dumps(headers_dict, indent=2)}\n"
                f"Response Body: {response_body}")

    def get(self, endpoint, params=None, headers=None):
        """
        Send GET request
        """
        request_headers = self.get_headers(headers)
        logger.info(f"Sending GET request to {self.base_url}{endpoint}")
        logger.info(f"Headers: {json.dumps(request_headers, indent=2)}")
        if params:
            logger.info(f"Query Parameters: {json.dumps(params, indent=2)}")
        
        # Attach request details to Allure report
        with allure.step(f"Sending GET request to {self.base_url}{endpoint}"):
            attach_api_request(f"{self.base_url}{endpoint}", "GET", request_headers, params=params)
            
            response = self.api_context.get(
                endpoint,
                params=params,
                headers=request_headers
            )
            
            # Attach response to Allure report
            attach_api_response(response)
            logger.info(self.format_response_log(response))
            return response

    def post(self, endpoint, data=None, json_data=None, headers=None, form_data=None):
        """
        Send POST request
        """
        request_headers = self.get_headers(headers)
        logger.info(f"Sending POST request to {self.base_url}{endpoint}")
        logger.info(f"Headers: {json.dumps(request_headers, indent=2)}")
        
        # Handle JSON data by serializing it
        if json_data:
            logger.info(f"JSON Data: {json.dumps(json_data, indent=2)}")
            # Serialize JSON data and ensure Content-Type is application/json
            data = json.dumps(json_data)
            request_headers["Content-Type"] = "application/json"
        
        if data and not isinstance(data, str) and not json_data:
            logger.info(f"Form Data: {data}")
        
        if form_data:
            logger.info(f"Multipart Form Data: {form_data}")
        
        # Attach request details to Allure report
        with allure.step(f"Sending POST request to {self.base_url}{endpoint}"):
            attach_api_request(f"{self.base_url}{endpoint}", "POST", request_headers, data, json_data)
            
            response = self.api_context.post(
                endpoint,
                data=data,
                headers=request_headers,
                form=form_data
            )
            
            # Attach response to Allure report
            attach_api_response(response)
            logger.info(self.format_response_log(response))
            return response

    def put(self, endpoint, data=None, json_data=None, headers=None):
        """
        Send PUT request
        """
        request_headers = self.get_headers(headers)
        logger.info(f"Sending PUT request to {self.base_url}{endpoint}")
        logger.info(f"Headers: {json.dumps(request_headers, indent=2)}")
        
        # Handle JSON data by serializing it
        if json_data:
            logger.info(f"JSON Data: {json.dumps(json_data, indent=2)}")
            # Serialize JSON data and ensure Content-Type is application/json
            data = json.dumps(json_data)
            request_headers["Content-Type"] = "application/json"
        
        if data and not isinstance(data, str) and not json_data:
            logger.info(f"Form Data: {data}")
        
        # Attach request details to Allure report
        with allure.step(f"Sending PUT request to {self.base_url}{endpoint}"):
            attach_api_request(f"{self.base_url}{endpoint}", "PUT", request_headers, data, json_data)
            
            response = self.api_context.put(
                endpoint,
                data=data,
                headers=request_headers
            )
            
            # Attach response to Allure report
            attach_api_response(response)
            logger.info(self.format_response_log(response))
            return response

    def delete(self, endpoint, params=None, headers=None):
        """
        Send DELETE request
        """
        request_headers = self.get_headers(headers)
        logger.info(f"Sending DELETE request to {self.base_url}{endpoint}")
        logger.info(f"Headers: {json.dumps(request_headers, indent=2)}")
        
        if params:
            logger.info(f"Query Parameters: {json.dumps(params, indent=2)}")
        
        # Attach request details to Allure report
        with allure.step(f"Sending DELETE request to {self.base_url}{endpoint}"):
            attach_api_request(f"{self.base_url}{endpoint}", "DELETE", request_headers, params=params)
            
            response = self.api_context.delete(
                endpoint,
                params=params,
                headers=request_headers
            )
            
            # Attach response to Allure report
            attach_api_response(response)
            logger.info(self.format_response_log(response))
            return response

    def patch(self, endpoint, data=None, json_data=None, headers=None):
        """
        Send PATCH request
        """
        request_headers = self.get_headers(headers)
        logger.info(f"Sending PATCH request to {self.base_url}{endpoint}")
        logger.info(f"Headers: {json.dumps(request_headers, indent=2)}")
        
        # Handle JSON data by serializing it
        if json_data:
            logger.info(f"JSON Data: {json.dumps(json_data, indent=2)}")
            # Serialize JSON data and ensure Content-Type is application/json
            data = json.dumps(json_data)
            request_headers["Content-Type"] = "application/json"
        
        if data and not isinstance(data, str) and not json_data:
            logger.info(f"Form Data: {data}")
        
        # Attach request details to Allure report
        with allure.step(f"Sending PATCH request to {self.base_url}{endpoint}"):
            attach_api_request(f"{self.base_url}{endpoint}", "PATCH", request_headers, data, json_data)
            
            response = self.api_context.patch(
                endpoint,
                data=data,
                headers=request_headers
            )
            
            # Attach response to Allure report
            attach_api_response(response)
            logger.info(self.format_response_log(response))
            return response

    def get_token(self, user_credentials):
        """
        Get authentication token
        """
        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        
        logger.info(f"Getting authentication token for user: {user_email}")
        
        with allure.step(f"Getting authentication token for user: {user_email}"):
            response = self.post(
                "/api/ecom/auth/login",
                data={"userEmail": user_email, "userPassword": user_password}
            )
            
            assert response.ok, f"Failed to get token: {response.status} {response.text()}"
            
            response_json = response.json()
            token = response_json["token"]
            
            logger.info(f"Authentication token obtained successfully")
            return token

    def create_order(self, product_id, country="India"):
        """
        Create a new order
        """
        logger.info(f"Creating order for product ID: {product_id}")
        
        with allure.step(f"Creating order for product ID: {product_id}"):
            response = self.post(
                "/api/ecom/order/create-order",
                data={"orders": [{"country": country, "productOrderedId": product_id}]}
            )
            
            assert response.status == 201, f"Failed to create order: {response.status} {response.text()}"
            
            response_body = response.json()
            order_id = response_body["orders"][0]
            
            logger.info(f"Order created successfully with ID: {order_id}")
            return order_id

    def get_order_details(self, order_id):
        """
        Get details of a specific order
        """
        logger.info(f"Getting details for order ID: {order_id}")
        
        with allure.step(f"Getting details for order ID: {order_id}"):
            response = self.get(f"/api/ecom/order/get-orders-details?id={order_id}")
            
            assert response.ok, f"Failed to get order details: {response.status} {response.text()}"
            
            order_details = response.json()
            logger.info(f"Order details retrieved successfully")
            
            return order_details

    def get_orders(self):
        """
        Get all orders
        """
        logger.info("Getting all orders")
        
        with allure.step("Getting all orders"):
            response = self.get("/api/ecom/order/get-orders-for-customer")
            
            assert response.ok, f"Failed to get orders: {response.status} {response.text()}"
            
            orders = response.json()
            logger.info(f"Retrieved {len(orders['data'])} orders")
            
            return orders
