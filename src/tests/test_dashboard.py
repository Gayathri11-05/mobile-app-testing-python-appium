"""Dashboard feature test cases."""

import pytest
from src.config.config import Config
from src.pages.dashboard_page import DashboardPage
from src.utilities.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.mark.dashboard
@pytest.mark.smoke
class TestDashboard:
    """Test suite for Dashboard functionality."""

    @pytest.mark.android
    def test_open_dashboard_android(self, driver):
        """
        Test navigation through Dashboard on Android.

        Steps:
        1. Launch app and navigate to Dashboard
        2. Click dashboard button
        3. Click navigation icons
        4. Verify dashboard loaded successfully

        Expected Result:
        - Dashboard elements should be clickable
        - No errors should occur
        """
        logger.info("Starting test: test_open_dashboard_android")

        dashboard_page = DashboardPage(driver)

        # Run only if platform is Android
        if Config.is_android():
            assert dashboard_page.open_dashboard_android(), \
                "Failed to navigate Dashboard on Android"
            logger.info("Dashboard navigation successful on Android.")
        else:
            pytest.skip("Skipping Android test on non-Android platform")

        logger.info("Test passed: test_open_dashboard_android")

    @pytest.mark.ios
    def test_open_dashboard_ios(self, driver):
        """
        Test navigation through Dashboard on iOS.

        Steps:
        1. Launch app and navigate to Dashboard
        2. Click through all dashboard elements
        3. Verify Account Balance Summary is accessible
        4. Verify back navigation works correctly

        Expected Result:
        - Dashboard flow should complete without failure
        """
        logger.info("Starting test: test_open_dashboard_ios")

        dashboard_page = DashboardPage(driver)

        # Run only if platform is iOS
        if Config.is_ios():
            assert dashboard_page.open_dashboard_ios(), \
                "Failed to navigate Dashboard on iOS"
            logger.info("Dashboard navigation successful on iOS.")
        else:
            pytest.skip("Skipping iOS test on non-iOS platform")

        logger.info("Test passed: test_open_dashboard_ios")

    @pytest.mark.regression
    def test_dashboard_cross_platform(self, driver):
        """
        Unified dashboard test (cross-platform).

        Steps:
        1. Launch app
        2. Automatically detect platform (Android/iOS)
        3. Perform dashboard navigation

        Expected Result:
        - Dashboard flow should work on both platforms
        """
        logger.info("Starting test: test_dashboard_cross_platform")

        dashboard_page = DashboardPage(driver)
        assert dashboard_page.open_dashboard(), \
            "Dashboard flow failed on current platform"

        logger.info("Test passed: test_dashboard_cross_platform")
