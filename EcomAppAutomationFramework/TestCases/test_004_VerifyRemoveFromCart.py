import pytest
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from EcomAppAutomationFramework.PageObjects.cartPage import cartPage
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.integration
def test_remove_from_cart(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    logger.info("Navigated to login page")
    
    # Login with valid credentials
    DashboardPage = LoginPage.loginToApp("av1234@gmail.com", "Bulbul@123")
    logger.info("Logged in successfully")
    
    # Add product to cart first
    DashboardPage.add_product_to_cart("ZARA COAT 3")
    logger.info("Added product to cart")
    
    # Navigate to cart and remove the product
    CartPage = cartPage(browserInstance)
    CartPage.navigate_to_cart()
    assert CartPage.verify_product_in_cart("ZARA COAT 3")
    logger.info("Verified product is in cart before removal")
    CartPage.remove_product_from_cart("ZARA COAT 3")
    browserInstance.wait_for_timeout(1000)  # Wait for UI to update
    assert CartPage.is_cart_empty()
    logger.info("Verified product is removed from cart") 