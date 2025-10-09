"""Account page object for Digital Bank App."""

from appium.webdriver.common.appiumby import AppiumBy as By, AppiumBy
from pages.base_page import BasePage


class AccountPage(BasePage):
    """
    Account page object for Android version of Digital Bank App.
    Handles navigation and actions related to account details.
    """

    # Android Locators
    WELCOME_TEXT = (By.ID,
    "xyz.digitalbank.demo:id/welcomeText"
    )
    TOOLBAR_IMAGE = (By.ID,
    "xyz.digitalbank.demo:id/toolbar_image"
    )
    NAME = (By.ID,
    "xyz.digitalbank.demo:id/name"
    )
    ACCOUNT_DETAILS = (By.ID,
    "xyz.digitalbank.demo:id/accountDetailsLayout"
    )
    SELECT_ACCOUNT = (By.ID,
    "xyz.digitalbank.demo:id/selectAccountText"
    )
    TEXT1 = (By.ID,
    "android:id/text1"
    )
    INDIVIDUAL_SAVINGS = (By.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Individual Savings - 1000075.0")'
    )
    ACCOUNT_SPINNER = (By.ID,
    "xyz.digitalbank.demo:id/accountSpinner"
    )
    TEST_ACCOUNT = (
        By.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Test - 1003.0")'
    )
    INDIVIDUAL_CHECKING = (
        By.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Individual Checking - 846.0")'
    )
    TABLE_ROW = (
        By.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.widget.TableRow").instance(0)'
    )
    ONLINE_WITHDRAWAL = (
        By.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Online Withdrawl").instance(0)'
    )
    ONLINE_DEPOSIT = (
        By.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Online Deposit").instance(0)'
    )
    AMOUNT_5 = (
        By.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("5.0").instance(0)'
    )
    AMOUNT_848 = (
        By.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("848.0").instance(0)'
    )

    # iOS Locators
    IOS_WELCOME_TEXT = (AppiumBy.IOS_CLASS_CHAIN,
    '**/XCUIElementTypeStaticText[`name == "Welcome"`]'
    )
    IOS_USER_NAME = (AppiumBy.ACCESSIBILITY_ID,
    " Mr. Josh Smith"
    )
    IOS_ACCOUNT_NUMBER = (AppiumBy.ACCESSIBILITY_ID,
    "486136373"
    )
    IOS_ACCOUNT_TYPE = (AppiumBy.ACCESSIBILITY_ID,
    "Individual Savings"
    )
    IOS_BALANCE = (AppiumBy.IOS_CLASS_CHAIN,
    '**/XCUIElementTypeStaticText[`name == "1000393.0"`][1]'
    )
    IOS_PICKER_WHEEL = (AppiumBy.CLASS_NAME,
    "XCUIElementTypePickerWheel"
    )
    IOS_TRANSACTION_ROW = (AppiumBy.IOS_CLASS_CHAIN,
    '**/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[28]/XCUIElementTypeOther[1]/XCUIElementTypeOther'
    )
    IOS_TRANSACTION_DESC = (AppiumBy.ACCESSIBILITY_ID,
    "hfhfh"
    )
    IOS_TRANSACTION_DATE = (AppiumBy.IOS_CLASS_CHAIN,
    '**/XCUIElementTypeStaticText[`name == "7 September 2025"`][2]'
    )

    def __init__(self, driver):
        """Initialize AccountPage."""
        super().__init__(driver)
        self.config = None

    # Android Actions
    def open_account_details_android(self):
        """Perform full account detail navigation."""
        self.logger.info("Navigating through account details (Android)")

        steps = [
            self.actions.click(self.WELCOME_TEXT),
            self.actions.click(self.TOOLBAR_IMAGE),
            self.actions.click(self.NAME),
            self.actions.click(self.ACCOUNT_DETAILS),
            self.actions.click(self.SELECT_ACCOUNT),
            self.actions.click(self.TEXT1),
            self.actions.click(self.INDIVIDUAL_SAVINGS),
            self.actions.click(self.ACCOUNT_SPINNER),
            self.actions.click(self.TEST_ACCOUNT),
            self.actions.click(self.TEXT1),
            self.actions.click (self.INDIVIDUAL_CHECKING),
            self.actions.click(self.TABLE_ROW),
            self.actions.click(self.ONLINE_WITHDRAWAL),
            self.actions.click(self.ONLINE_DEPOSIT),
            self.actions.click(self.AMOUNT_5),
            self.actions.click(self.AMOUNT_848)
        ]

        self.logger.info("Account details navigation completed successfully.")
        return True

    def open_account_details_ios(self):
        """Perform actions to open and verify account details."""
        self.actions.click(self.IOS_WELCOME_TEXT)
        self.actions.click(self.IOS_USER_NAME)
        self.actions.click(self.IOS_ACCOUNT_NUMBER)
        self.actions.click(self.IOS_ACCOUNT_TYPE)
        self.actions.click(self.IOS_BALANCE)
        self.actions.click(self.IOS_PICKER_WHEEL)
        self.actions.click(self.IOS_PICKER_WHEEL)  # double click as per sequence
        self.actions.click(self.IOS_TRANSACTION_ROW)
        self.actions.click(self.IOS_TRANSACTION_DESC)
        self.actions.click(self.IOS_TRANSACTION_DATE)
        return True

# Unified Action (Auto-select platform)

    def AccountPage(self):
        """
        Open dashboard based on current platform.

        Returns:
            bool: True if successful, False otherwise
        """
        if self.config.is_android():
            return self.open_account_details_android()
        else:
            return self.open_account_details_ios()
