<!--
    #/**
    # * @author Avdhut Shirgaonkar
    # * Email: avdhut.ssh@gmail.com
    # * LinkedIn: https://www.linkedin.com/in/avdhut-shirgaonkar-811243136/
    # */
    #/***************************************************/
-->

# 💻 UI & API Automation Using Playwright with Python

## 📑 Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Test Execution](#test-execution)
- [Data-Driven Testing](#data-driven-testing)
- [BDD Tests](#bdd-tests)
- [Reporting](#reporting)
- [CI/CD Using GitHub Actions](#cicd-using-github-actions)
- [Contacts](#contacts)

## 📖 Introduction

This repository contains a comprehensive automation framework built with **Playwright** and **Python**, designed to automate both UI and API tests. The framework follows the Page Object Model (POM) pattern, which separates test logic from the UI structure, enhancing maintainability and reusability. Test execution is managed through **pytest**, with parallel test execution capabilities for faster results.

The framework includes features like detailed **Allure reporting** with screenshots captured at critical points, API payload attachments, and comprehensive test results. It also leverages Object-Oriented Programming principles for code organization and reusability.

Key features include:
- Hybrid architecture supporting both UI and API automation
- Optional (Just for Demo) BDD test approach using Cucumber-style Gherkin syntax with pytest-bdd
- Comprehensive logging and exception handling
- Screenshot capture for all validations and failures
- API request/response payload capture for detailed analysis
- Cross-browser testing support (Chrome, Firefox, WebKit)

## 🛠️ Prerequisites

Before you start, ensure you have the following installed on your machine:

- **Python**: Version 3.8 or later
- **Pip**: Python package manager
- **Git**: To clone the repository
- **Allure**: For detailed reporting (optional, but recommended)

## 📁 Project Structure

This project follows a modular architecture designed for scalability and maintainability. Below is the high-level structure of the project:

```plaintext
| EcomAppAutomationFramework/
├── PageObjects/                        # Page Object classes for different website pages
│   ├── loginPage.py                    # Handles login page interactions
│   ├── dashboardPage.py                # Dashboard page interactions
│   ├── cartPage.py                     # Cart page interactions
│   ├── checkoutPage.py                 # Checkout page interactions
│   ├── orderDetailsPage.py             # Order details page interactions
│   └── ordersPage.py                   # Orders page interactions
├── TestCases/                          # Test scripts
│   ├── test_001_VerifyPlaceOrder.py    # Tests for order placement
│   ├── test_002_VerifyInvalidLogin.py  # Tests for invalid login attempts
│   ├── test_003_VerifyAddToCart.py     # Tests for adding products to cart
│   ├── test_004_VerifyRemoveFromCart.py # Tests for removing products from cart
│   ├── test_005_VerifyProductSearch.py # Tests for product search functionality
│   ├── conftest.py                     # Pytest fixtures and configuration
├── API_Utils/                          # API testing utilities
│   ├── API_Client.py                   # Generic API client with methods for HTTP requests
│   ├── API_Factory.py                  # Factory pattern implementation for API testing
├── Common_Utils/                       # Shared utilities
│   ├── logger.py                       # Custom logging implementation
│   ├── allure_utils.py                 # Utilities for Allure reporting
├── TestData/                           # Test data files
│   └── creds.json                      # Credentials and test data in JSON format
├── BDD/                                # Behavior-Driven Development tests
│   ├── features/                       # Gherkin feature files
│   │   └── e2e.feature                 # Feature file for E2E scenarios
│   ├── step_definitions/               # Step implementation files
│   │   └── e2e_steps.py                # Steps implementation for e2e.feature
├── allure-results/                     # Generated Allure results
├── allure-report/                      # Generated Allure report
├── requirements.txt                    # Python dependencies
└── pytest.ini                          # Pytest configuration
```

## ▶️ Getting Started

1. Clone the repository:

```bash
git clone https://github.com/avdhutssh/Playwright-Pytest.git
```

2. Navigate to the project directory:

```bash
cd Playwright-Pytest
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Test Execution

You can run the tests using pytest with various options:

### Run all tests:

```bash
pytest EcomAppAutomationFramework/TestCases/
```

### Run a specific test:

```bash
pytest EcomAppAutomationFramework/TestCases/test_001_VerifyPlaceOrder.py
```

### Run tests with Allure reporting:

```bash
pytest EcomAppAutomationFramework/TestCases/ --alluredir=./allure-results
```

### Run tests with browser UI visible:

```bash
pytest EcomAppAutomationFramework/TestCases/ --headed
```

### Run tests on a specific browser:

```bash
pytest EcomAppAutomationFramework/TestCases/ --browser_name=firefox
```
Available options: `chrome` (default), `firefox`, `webkit`

### Generate and view Allure report:

```bash
allure serve ./allure-results
```

## 📊 Data-Driven Testing

The framework supports data-driven testing using parameterization in pytest. Test data is stored in JSON files and loaded dynamically during test execution.

Example of data-driven test:

```python
@pytest.mark.parametrize('user_credentials', users_data)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):
    username = user_credentials['userEmail']
    password = user_credentials['userPassword']
    # Test steps using the provided credentials
```

## 🎯 Reporting

This project integrates **Allure Reports** for detailed test execution reporting, including:

- Test execution results with pass/fail status
- Detailed logs from each test step
- Screenshots captured during test execution
- API request and response payloads
- Test execution timeline and duration

To view the reports:

1. Run tests with Allure reporting enabled
2. Generate and open the report

![Allure Report](/Misc/AllureReport.png)

## 📧 Contacts

- [![Email](https://img.shields.io/badge/Email-avdhut.ssh@gmail.com-green)](mailto:avdhut.ssh@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/avdhut-shirgaonkar-811243136/)

Feel free to reach out if you have any questions, or suggestions.

Happy Testing!

Avdhut Shirgaonkar
