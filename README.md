# E2E Test Automation Framework — saucedemo + JSONPlaceholder

A Python-based test automation framework demonstrating end-to-end UI testing with Selenium and REST API testing with Requests. Built as a portfolio project showcasing real-world QA patterns including Page Object Model, fixtures, parametrized tests, and CI/CD integration.

[![Test Suite](https://github.com/athulyabiju23/saucedemo-test-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/athulyabiju23/saucedemo-test-automation/actions/workflows/tests.yml)

## Overview

This project demonstrates a layered testing approach against two complementary target applications:

- **UI Layer:** [saucedemo.com](https://www.saucedemo.com/) — an e-commerce demo site
- **API Layer:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a free REST API for testing

23 automated tests cover login, cart, checkout, and REST CRUD operations with both positive and negative scenarios.

## Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.11 |
| UI Automation | Selenium WebDriver 4.x |
| API Testing | Python Requests |
| Test Framework | Pytest |
| Architecture | Page Object Model (POM) |
| Driver Management | webdriver-manager (auto-downloads ChromeDriver) |
| CI/CD | GitHub Actions |
| Browser | Chrome / Chromium |

## Project Structure
''''
saucedemo-test-automation/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions CI/CD
├── pages/                      # Page Object Model
│   ├── base_page.py            # Shared methods (waits, click, type)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                      # UI tests (Selenium)
│   ├── conftest.py             # Pytest fixtures (browser setup)
│   ├── test_login.py           # 7 login scenarios
│   └── test_cart_and_checkout.py  # 6 cart/checkout flows
├── api_tests/                  # API tests (Requests)
│   ├── conftest.py             # Base URL and headers fixtures
│   ├── test_users_api.py       # 5 user endpoint tests
│   └── test_posts_api.py       # 5 posts endpoint tests
├── bugs/                       # Documented bug reports
│   ├── BUG-001-cart-badge-empty-state.md
│   └── BUG-002-checkout-postal-code-validation.md
├── requirements.txt
└── README.md
''''

## What's Tested

### UI Tests (13 tests against saucedemo.com)

**Login Suite — 7 tests**
- Successful login with valid credentials
- Locked user rejection
- Wrong password handling
- Empty credentials validation
- Parametrized negative scenarios (3 variations)

**Cart & Checkout Suite — 6 tests**
- Adding single item to cart
- Adding multiple items
- Removing items from cart
- Cart page displays correct items
- Complete checkout flow (info → review → confirm)
- Checkout validation (missing first name)

### API Tests (10 tests against JSONPlaceholder)

**Users API — 5 tests**
- GET all users returns 200 + valid list
- Single user response schema validation
- Type and format validation (e.g., email contains `@`)
- 404 for nonexistent users
- Response time SLA assertion (< 2s)

**Posts API — 5 tests**
- GET all posts returns 200
- POST create new post returns 201 with echoed data
- PUT update existing post returns 200
- DELETE post returns 200
- Filter posts by userId query parameter

## Key Patterns Demonstrated

- **Page Object Model:** All Selenium interactions abstracted into page classes; tests are readable business steps
- **Explicit Waits:** `WebDriverWait` with `ExpectedConditions` instead of fragile `time.sleep()`
- **Pytest Fixtures:** Reusable browser and API setup/teardown via `conftest.py`
- **Parametrized Tests:** Data-driven testing with `@pytest.mark.parametrize`
- **Dynamic Locators:** Build locators at runtime (e.g., add-to-cart buttons by product name)
- **Schema Validation:** Verify API response structure and types
- **Negative Testing:** Equal coverage of failure scenarios alongside happy paths
- **CI/CD Integration:** GitHub Actions runs all tests on every push

## Setup

### Prerequisites
- Python 3.8+
- Chrome browser
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/athulyabiju23/saucedemo-test-automation.git
cd saucedemo-test-automation

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest -v

# Run only UI tests
pytest tests/ -v

# Run only API tests
pytest api_tests/ -v

# Run a specific test
pytest tests/test_login.py::TestLogin::test_successful_login_with_valid_credentials -v

# Run in headless mode (no browser window)
HEADLESS=true pytest tests/ -v
```

## CI/CD

Every push to `main` triggers the GitHub Actions workflow which:

1. Sets up Python 3.11 on Ubuntu
2. Installs project dependencies
3. Runs API tests
4. Sets up Chrome and runs UI tests in headless mode
5. Reports pass/fail status

View the latest run in the [Actions tab](https://github.com/athulyabiju23/saucedemo-test-automation/actions).

## Documented Bugs

Two example bug reports are included in the `bugs/` folder, demonstrating how findings would be documented in a real QA workflow with severity, priority, reproduction steps, and recommendations:

- [BUG-001: Cart Badge Empty State](bugs/BUG-001-cart-badge-empty-state.md) — DOM removal causes automation edge case
- [BUG-002: Checkout Postal Code Validation](bugs/BUG-002-checkout-postal-code-validation.md) — Missing input validation

## Future Improvements

Things I would add next given more time:

- Allure reporting with screenshots on failure
- Parallel test execution via `pytest-xdist`
- Cross-browser testing (Firefox, Edge) via Selenium Grid or Playwright
- Data-driven test cases loading from external CSV/JSON
- Visual regression testing
- Performance testing layer with Locust (echoing my Honeywell experience with JMeter and Locust at scale)

## About

Built by Athulya Biju as part of preparing for SDET / QA Automation roles. 1.5 years of prior performance and automation testing experience at Honeywell on enterprise IoT platforms using JMeter, Locust, Selenium WebDriver Sampler, and Postman.

- LinkedIn: [linkedin.com/in/athulyabiju](https://linkedin.com/in/athulyabiju)
- GitHub: [github.com/athulyabiju23](https://github.com/athulyabiju23)