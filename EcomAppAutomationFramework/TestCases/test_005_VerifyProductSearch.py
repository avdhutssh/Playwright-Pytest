import pytest
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage

@pytest.mark.integration
def test_product_search(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    
    DashboardPage = LoginPage.loginToApp("av1234@gmail.com", "Bulbul@123")
    
    DashboardPage.search_product("ZARA")
    
    browserInstance.wait_for_timeout(1000)
    
    assert DashboardPage.is_product_search_result_displayed("ZARA") 