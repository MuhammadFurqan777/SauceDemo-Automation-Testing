
import pytest
import os
import re
from selenium import webdriver


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    browser = webdriver.Chrome(options=options)

    browser.maximize_window()

    yield browser

    browser.quit()


# Capture screenshot automatically when a test fails

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        browser = item.funcargs.get("driver")

        if browser:

            os.makedirs("screenshots", exist_ok=True)

            safe_name = re.sub(
                r"[^a-zA-Z0-9_-]", "_", item.name
            )

            screenshot_path = (
                f"screenshots/{safe_name}.png"
            )

            browser.save_screenshot(screenshot_path)

            print(f"\nScreenshot saved: {screenshot_path}")
