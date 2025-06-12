import pytest
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.integration
def test_product_search(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    logger.info("Navigated to login page")
    
    # Login with valid credentials
    DashboardPage = LoginPage.loginToApp("av1234@gmail.com", "Bulbul@123")
    logger.info("Logged in successfully")
    
    # Search for a product
    DashboardPage.search_product("ZARA")
    logger.info("Searched for product: ZARA")
    
    # Wait for search results
    browserInstance.wait_for_timeout(1000)
    
    # Verify search results
    assert DashboardPage.is_product_search_result_displayed("ZARA")
    logger.info("Verified product search result is displayed") 