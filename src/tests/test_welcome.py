"""Account feature test cases."""

import pytest
from src.pages.welcome_page import AccountPage
from src.utilities.logger import Logger
from src.config.config import Config

logger = Logger.get_logger(__name__)


@pytest.mark.account
@pytest.mark.smoke
class TestAccount:
    """Test suite for Account page functionality."""

    def test_open_account_details_android(self, driver):
        """
        Test navigation through Account Details on Android.

        Steps:
        1. Launch app
        2. Navigate through account details and transactions

        Expected Result:
        - All elements should be accessible and clickable
        - Flow completes without exception
        """
        logger.info("Starting test: test_open_account_details_android")

        account_page = AccountPage(driver)

        if Config.is_android():
            assert account_page.open_account_details(), \
                "Failed to navigate account details on Android"
            logger.info("Account details navigation successful on Android.")
        else:
            pytest.skip("Skipping Android test on non-Android platform")

        logger.info("Test passed: test_open_account_details_android")

    @pytest.mark.ios
    class TestAccountPage:
        """Test suite for iOS account page."""

        def test_open_account_details_ios(self, driver):
            """
            Validate that user can navigate through account details successfully.
             Steps:
        1. Launch app
        2. Navigate through account details and transactions

        Expected Result:
        - All elements should be accessible and clickable
        - Flow completes without exception
            """
            logger.info("Starting test: test_open_account_details_ios")

            account_page = AccountPage(driver)

            assert account_page.open_account_details(), \
                "Failed to navigate account details on ios"


            logger.info("Test passed: test_open_account_details_ios")