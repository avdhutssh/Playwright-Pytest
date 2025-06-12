import pytest
from playwright.sync_api import Playwright
from EcomAppAutomationFramework.API_Utils.API_Client import API_Client
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

class API_Factory:
    def __init__(self):
        self.api_client = None
        logger.info("API Factory initialized")

    def initialize_client(self, playwright: Playwright, base_url="https://rahulshettyacademy.com"):
        """
        Initialize API client with Playwright context
        """
        self.api_client = API_Client(playwright, base_url)
        logger.info(f"API Client initialized with base URL: {base_url}")
        return self.api_client

    def get_headers(self, playwright: Playwright, user_credentials):
        """
        Get headers with authentication token
        """
        if not self.api_client:
            self.initialize_client(playwright)
            
        token = self.get_token(playwright, user_credentials)
        headers = {
            "Authorization": token,
            "Accept": "application/json"
        }
        logger.info("Headers with authentication token created")
        return headers

    def get_token(self, playwright: Playwright, user_credentials):
        """
        Get authentication token
        """
        if not self.api_client:
            self.initialize_client(playwright)
            
        token = self.api_client.get_token(user_credentials)
        self.api_client.set_authorization(token)
        logger.info("Authentication token obtained and set in API client")
        return token

    def createOrder(self, playwright: Playwright, productId, user_credentials):
        """
        Create a new order
        """
        if not self.api_client:
            self.initialize_client(playwright)
            
        # Get token and set authorization
        token = self.get_token(playwright, user_credentials)
        self.api_client.set_authorization(token)
        
        # Create order
        order_id = self.api_client.create_order(productId)
        logger.info(f"Order created with ID: {order_id}")
        return order_id

    def get_order_details(self, playwright: Playwright, order_id, user_credentials):
        """
        Get details of a specific order
        """
        if not self.api_client:
            self.initialize_client(playwright)
            
        # Get token and set authorization
        token = self.get_token(playwright, user_credentials)
        self.api_client.set_authorization(token)
        
        # Get order details
        order_details = self.api_client.get_order_details(order_id)
        logger.info(f"Retrieved details for order ID: {order_id}")
        return order_details

    def get_all_orders(self, playwright: Playwright, user_credentials):
        """
        Get all orders for the customer
        """
        if not self.api_client:
            self.initialize_client(playwright)
            
        # Get token and set authorization
        token = self.get_token(playwright, user_credentials)
        self.api_client.set_authorization(token)
        
        # Get all orders
        orders = self.api_client.get_orders()
        logger.info("Retrieved all orders for the customer")
        return orders