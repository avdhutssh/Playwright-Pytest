import pytest
from EcomAppAutomationFramework.PageObjects.loginPage import loginPage
from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage
from EcomAppAutomationFramework.PageObjects.cartPage import cartPage

@pytest.mark.integration
def test_add_to_cart(browserInstance):
    LoginPage = loginPage(browserInstance)
    LoginPage.navigate_to_login()
    
    DashboardPage = LoginPage.loginToApp("av1234@gmail.com", "Bulbul@123")
    
    DashboardPage.add_product_to_cart("ZARA COAT 3")
    
    CartPage = DashboardPage.navigate_to_cart()
    
    assert CartPage.verify_product_in_cart("ZARA COAT 3") 