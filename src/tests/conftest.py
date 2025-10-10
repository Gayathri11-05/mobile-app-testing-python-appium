"""Pytest configuration and shared fixtures for Perfecto Mobile Cloud."""

import pytest
from typing import Generator
from selenium.webdriver.remote.webdriver import WebDriver
from src.utilities.driver_factory import DriverFactory
from src.utilities.logger import Logger
from src.utilities.mobile_actions import MobileActions

logger = Logger.get_logger(__name__)


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    """
    Create and provide driver instance for each test.

    Yields:
        WebDriver: Perfecto Appium driver instance.

    This fixture:
    - Creates a new driver before each test
    - Yields the driver to the test
    - Quits the driver after test completion to release Perfecto session
    """
    logger.info("=" * 80)
    logger.info("Setting up driver for test")

    driver_instance = None
    try:
        driver_instance = DriverFactory.create_driver()
        logger.info("Perfecto driver session created successfully.")
        yield driver_instance
    except Exception as e:
        logger.error(f"Error during driver setup: {e}")
        raise
    finally:
        if driver_instance:
            try:
                logger.info("Tearing down driver after test...")
                driver_instance.quit()
                logger.info("Perfecto driver session closed successfully.")
            except Exception as quit_error:
                logger.warning(f"Error during driver.quit(): {quit_error}")
        else:
            logger.warning("Driver instance was not created; skipping quit().")

    logger.info("=" * 80)


@pytest.fixture(scope="function")
def take_screenshot_on_failure(driver: WebDriver, request: pytest.FixtureRequest):
    """
    Automatically take screenshot on test failure.

    Args:
        driver (WebDriver): Driver fixture
        request (pytest.FixtureRequest): Pytest request object
    """
    yield

    # Capture screenshot only if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        actions = MobileActions(driver)
        test_name = request.node.name
        try:
            actions.take_screenshot(f"failure_{test_name}")
            logger.info(f"Screenshot taken for failed test: {test_name}")
        except Exception as err:
            logger.warning(f"Failed to take screenshot for {test_name}: {err}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    """
    Hook to make test result available to fixtures.

    Makes the test result accessible to other fixtures for
    conditional actions like taking screenshots on failure.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def pytest_configure(config: pytest.Config):
    """
    Configure pytest with custom markers.

    Args:
        config (pytest.Config): Pytest config object
    """
    config.addinivalue_line("markers", "smoke: Mark test as smoke test")
    config.addinivalue_line("markers", "regression: Mark test as regression test")
    config.addinivalue_line("markers", "login: Mark test as login feature test")
    config.addinivalue_line("markers", "product: Mark test as product feature test")