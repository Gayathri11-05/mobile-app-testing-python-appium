"""Dashboard page object."""

from appium.webdriver.common.appiumby import AppiumBy as By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Dashboard page object for Digital Banking App.

    Handles navigation and actions on the dashboard screen
    for both Android and iOS platforms.
    """

    # Android Locators
  
    ANDROID_DASHBOARD_BUTTON = (
        By.ACCESSIBILITY_ID,
        "My Dashboard"
    )
    ANDROID_IMAGE_ICON = (
        By.CLASS_NAME,
        "android.widget.Image"
    )
    ANDROID_NAV_ICON = (
        By.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("xyz.digitalbank.demo:id/navigation_bar_item_icon_view").instance(2)'
    )

    # iOS Locators
    
    IOS_LOGIN_BUTTON = (
        By.ACCESSIBILITY_ID,
        "LogIn"
    )
    IOS_PIE_CHART_ICON = (
        By.ACCESSIBILITY_ID,
        "chart.pie.fill"
    )
    IOS_ACCOUNT_CELL_1 = (
        By.IOS_CLASS_CHAIN,
        "**/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/"
        "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
        "XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther"
    )
    IOS_ACCOUNT_CELL_2 = (
        By.IOS_CLASS_CHAIN,
        "**/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/"
        "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
        "XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther"
    )
    IOS_ACCOUNT_CELL_3 = (
        By.IOS_CLASS_CHAIN,
        "**/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/"
        "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
        "XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther"
    )
    IOS_BALANCE_SUMMARY = (
        By.ACCESSIBILITY_ID,
        "Account Balance Summary"
    )
    IOS_BACK_BUTTON = (
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeButton[`name == " "`]'
    )

    def __init__(self, driver):
        """
        Initialize DashboardPage.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        super().__init__(driver)

    # iOS Actions
    def open_dashboard_ios(self):
        """Navigate through dashboard options on iOS."""
        self.logger.info("Navigating Dashboard (iOS)")
        self.actions.click(self.IOS_LOGIN_BUTTON)
        self.actions.click(self.IOS_PIE_CHART_ICON)
        self.actions.click(self.IOS_ACCOUNT_CELL_1)
        self.actions.click(self.IOS_ACCOUNT_CELL_2)
        self.actions.click(self.IOS_ACCOUNT_CELL_3)
        self.actions.click(self.IOS_BALANCE_SUMMARY)
        self.actions.click(self.IOS_BACK_BUTTON)
        self.logger.info("iOS Dashboard navigation completed.")
        return True

    # Android Actions

    def open_dashboard_android(self):
        """Navigate to dashboard on Android."""
        self.logger.info("Navigating Dashboard (Android)")
        self.actions.click(self.ANDROID_DASHBOARD_BUTTON)
        self.actions.click(self.ANDROID_IMAGE_ICON)
        self.actions.click(self.ANDROID_NAV_ICON)
        self.logger.info("Android Dashboard navigation completed.")
        return True

    # Unified Action (Auto-select platform)

    def open_dashboard(self):
        """
        Open dashboard based on current platform.

        Returns:
            bool: True if successful, False otherwise
        """
        if self.config.is_android():
            return self.open_dashboard_android()
        else:
            return self.open_dashboard_ios()

