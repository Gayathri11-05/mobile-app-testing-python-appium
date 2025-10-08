"""Login feature test cases for Digital Banking App."""

import pytest
from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage  # Assuming dashboard page exists
from utilities.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    """Test suite for login functionality on both Android and iOS."""

    def test_successful_login(self, driver):
        """
        Test successful login with valid credentials.

        Steps:
        1. Navigate to login page
        2. Enter valid username and password
        3. Click login button
        4. Verify user is logged in successfully
        """
        logger.info("Starting test: test_successful_login")

        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        # Perform login
        assert login_page.login(
            Config.TEST_USERNAME,
            Config.TEST_PASSWORD
        ), "Login flow failed"

        # Verify login success by checking dashboard page
        assert dashboard_page.is_dashboard_displayed(), \
            "Dashboard page not displayed after login"

        logger.info("Test passed: test_successful_login")

    def test_login_with_invalid_credentials(self, driver):
        """
        Test login with invalid credentials.

        Steps:
        1. Navigate to login page
        2. Enter invalid username and password
        3. Click login button
        4. Verify error message is displayed
        """
        logger.info("Starting test: test_login_with_invalid_credentials")

        login_page = LoginPage(driver)

        # Attempt login with invalid credentials
        login_page.login("invalid@example.com", "wrongpassword")

        # Verify error message
        assert login_page.is_error_displayed(), \
            "Error message not displayed for invalid credentials"

        error_message = login_page.get_error_message()
        assert error_message != "", "Error message text is empty"

        logger.info(f"Error message displayed: {error_message}")
        logger.info("Test passed: test_login_with_invalid_credentials")

    def test_login_with_empty_username(self, driver):
        """
        Test login with empty username.

        Steps:
        1. Navigate to login page
        2. Leave username empty
        3. Enter password
        4. Click login button
        5. Verify error is displayed
        """
        logger.info("Starting test: test_login_with_empty_username")

        login_page = LoginPage(driver)

        # Attempt login with empty username
        login_page.navigate_to_login()
        login_page.enter_username("")
        login_page.enter_password(Config.TEST_PASSWORD)
        login_page.click_login_button()

        # Verify error
        assert login_page.is_error_displayed(), \
            "Error message not displayed for empty username"

        logger.info("Test passed: test_login_with_empty_username")

    @pytest.mark.regression
    def test_logout_functionality(self, driver):
        """
        Test logout functionality.

        Steps:
        1. Login with valid credentials
        2. Perform logout
        3. Verify user is logged out
        """
        logger.info("Starting test: test_logout_functionality")

        login_page = LoginPage(driver)

        # Login first
        assert login_page.login(
            Config.TEST_USERNAME,
            Config.TEST_PASSWORD
        ), "Login failed"

        # Perform logout
        assert login_page.logout(), "Logout failed"

        # Verify logout by navigating to login page again
        assert login_page.navigate_to_login(), \
            "Cannot navigate to login after logout"

        logger.info("Test passed: test_logout_functionality")
