from EcomAppAutomationFramework.PageObjects.dashboardPage import dashboardPage


class loginPage:
    def __init__(self,page):
        self.page = page
        self.username_input = page.get_by_placeholder("email@example.com")
        self.password_input = page.locator("#userPassword")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate_to_login(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def loginToApp(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return dashboardPage(self.page)