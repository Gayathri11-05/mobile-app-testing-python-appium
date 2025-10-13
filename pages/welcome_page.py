from appium.webdriver.common.appiumby import AppiumBy


class AccountPage:
    """Page Object for the Account screen in the Digital Bank app (iOS)."""

    # ---------- Locators ----------
    WELCOME_TEXT = (AppiumBy.IOS_PREDICATE, 'value == "Welcome"')
    USER_NAME = (AppiumBy.IOS_PREDICATE, 'name == "Mr. Josh Smith"')
    ACCOUNT_NUMBER = (AppiumBy.IOS_PREDICATE, 'label == "Account Number:"')
    ACCOUNT_TYPE = (AppiumBy.IOS_PREDICATE, 'label == "Account Type:"')
    ACCOUNT_SELECTION_PICKER = (
        AppiumBy.IOS_PREDICATE,
        'type == "XCUIElementTypePickerWheel"'
    )
    TRANSACTION_TABLE = (AppiumBy.IOS_PREDICATE, 'label == "Selected Account Summary"')

    # ---------- Constructor ----------
    def __init__(self, driver):
        self.driver = driver

    # ---------- Page Actions ----------
    def verify_welcome_text(self):
        """Verify the 'Welcome' text is visible."""
        return self.driver.find_element(*self.WELCOME_TEXT).is_displayed()

    def get_user_name(self):
        """Return the displayed user name."""
        element = self.driver.find_element(*self.USER_NAME)
        return element.get_attribute("label")

    def select_account(self, value="Individual Savings = 1000393.0"):
        """Select an account from the picker wheel."""
        picker = self.driver.find_element(*self.ACCOUNT_SELECTION_PICKER)
        picker.send_keys(value)
        return True

    def verify_transaction_table_visible(self):
        """Ensure the transaction summary section is displayed."""
        return self.driver.find_element(*self.TRANSACTION_TABLE).is_displayed()

    def open_account_details(self):
        """
        Example flow: verify all elements and simulate navigation.
        """
        try:
            assert self.verify_welcome_text(), "Welcome text not visible"
            assert self.get_user_name() == "Mr. Josh Smith", "User name mismatch"
            self.select_account()
            assert self.verify_transaction_table_visible(), "Transaction table not visible"
            return True
        except Exception as e:
            print(f"AccountPage verification failed: {e}")
            return False
