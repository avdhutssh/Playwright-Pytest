import pytest
import allure
from datetime import datetime
from EcomAppAutomationFramework.Common_Utils.allure_utils import attach_screenshot, attach_html


@pytest.fixture(scope="session")
def user_creds(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser to run tests on"
    )

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    context = browser.new_context(viewport=None)
    page = context.new_page()
    
    # Set test case name in Allure
    test_name = request.node.name
    allure.dynamic.title(test_name)
    
    # Attach browser information
    allure.dynamic.description(f"Browser: {browser_name}")
    
    # Start test
    yield page
    
    # Teardown
    context.close()
    browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    
    # Set test status in Allure
    if rep.when == "call" and rep.failed:
        try:
            # Try to get the browser instance
            browser = item.funcargs.get("browserInstance")
            if browser:
                try:
                    # Take screenshot on failure
                    screenshot = browser.screenshot()
                    allure.attach(
                        screenshot, 
                        name=f"Failure Screenshot - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception as e:
                    print(f"Warning: Could not attach failure screenshot: {e}")
                
                try:
                    # Get HTML source on failure
                    html_content = browser.content()
                    allure.attach(
                        html_content, 
                        name=f"HTML on Failure - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                        attachment_type=allure.attachment_type.HTML
                    )
                except Exception as e:
                    print(f"Warning: Could not attach failure HTML: {e}")
                
                try:
                    # Get URL on failure
                    url = browser.url
                    allure.attach(
                        url, 
                        name="URL on Failure", 
                        attachment_type=allure.attachment_type.TEXT
                    )
                except Exception as e:
                    print(f"Warning: Could not attach failure URL: {e}")
        except Exception as e:
            try:
                allure.attach(
                    str(e), 
                    name="Error capturing failure details", 
                    attachment_type=allure.attachment_type.TEXT
                )
            except:
                print(f"Warning: Could not attach error details: {e}")
            
    # Add test logs to Allure report
    if hasattr(item, "_report_sections"):
        for name, content, _ in item._report_sections:
            try:
                allure.attach(content, name=name, attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                print(f"Warning: Could not attach test log: {e}")