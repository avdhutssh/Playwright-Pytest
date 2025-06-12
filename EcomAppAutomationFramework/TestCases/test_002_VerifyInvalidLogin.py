import pytest
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.Common_Utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.integration
def test_invalid_login(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    logger.info("Navigated to login page")
    
    # Use completely invalid credentials
    LoginPage.loginToApp("invalid@example.com", "wrongpassword")
    
    # Verify error is displayed
    browserInstance.wait_for_timeout(1000) # Wait for error to appear
    assert LoginPage.is_login_error_displayed()
    logger.info("Verified error message for invalid login") 