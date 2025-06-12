import pytest
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage

@pytest.mark.integration
def test_invalid_login(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    
    LoginPage.loginToApp("invalid@example.com", "wrongpassword")
    
    browserInstance.wait_for_timeout(1000)
    assert LoginPage.is_login_error_displayed() 