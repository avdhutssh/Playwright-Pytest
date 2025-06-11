import pytest


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
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page
    context.tracing.stop(path=f"trace_{request.node.name}.zip")
    context.close()
    browser.close()