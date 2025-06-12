import pytest
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from EcomAppAutomationFramework.PageObjects.cartPage import cartPage
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.integration
def test_add_to_cart(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    logger.info("Navigated to login page")
    
    # Login with valid credentials
    DashboardPage = LoginPage.loginToApp("av1234@gmail.com", "Bulbul@123")
    logger.info("Logged in successfully")
    
    # Add product to cart
    DashboardPage.add_product_to_cart("ZARA COAT 3")
    logger.info("Added product to cart")
    
    # Navigate to cart
    CartPage = DashboardPage.navigate_to_cart()
    
    # Check if product is in cart
    assert CartPage.verify_product_in_cart("ZARA COAT 3")
    logger.info("Verified product is in cart") 