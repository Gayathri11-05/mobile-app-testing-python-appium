from appium.webdriver.common.appiumby import AppiumBy


class DepositPage:
    def __init__(self, driver):
        self.driver = driver
        self.platform = driver.capabilities.get("platformName", "").lower()

    # ===============================
    # LOCATORS
    # ===============================

    # --- Account Picker / Dropdown ---
    ANDROID_ACCOUNT_PICKER = (
        AppiumBy.XPATH,
        "//*[@resource-id='xyz.digitalbank.demo:id/accountSelect' or @content-desc='Account Picker']"
    )

    # --- Transaction Description ---
    ANDROID_TRANSACTION_DESC_FIELD = (
        AppiumBy.XPATH,
        "//*[@resource-id='xyz.digitalbank.demo:id/transactionDescriptionInput' or @content-desc='Enter Description']"
    )

    # --- Transaction Amount ---
    ANDROID_TRANSACTION_AMOUNT_FIELD = (
        AppiumBy.XPATH,
        "//*[@resource-id='xyz.digitalbank.demo:id/transactionAmountInput' or @content-desc='Enter Amount']"
    )

    # --- Create / Debit Switch ---
    ANDROID_CREATE_DEBIT_SWITCH = (
        AppiumBy.XPATH,
        "//*[@resource-id='xyz.digitalbank.demo:id/transactionSwitch' or @content-desc='Create or Debit']"
    )

    # --- Submit Button ---
    ANDROID_SUBMIT_BUTTON = (
        AppiumBy.XPATH,
        "//*[@resource-id='xyz.digitalbank.demo:id/submitButton' or @text='Submit']"
    )

    # --- iOS Locators ---
    IOS_ACCOUNT_PICKER = (
        AppiumBy.IOS_PREDICATE,
        "type == 'XCUIElementTypePickerWheel' AND value == 'Individual Savings = 1000075.0'"
    )

    IOS_TRANSACTION_DESC_FIELD = (
        AppiumBy.IOS_PREDICATE,
        "type == 'XCUIElementTypeTextField' AND value == 'Enter Description'"
    )

    IOS_TRANSACTION_AMOUNT_FIELD = (
        AppiumBy.IOS_PREDICATE,
        "type == 'XCUIElementTypeTextField' AND value == 'Enter Amount'"
    )

    IOS_CREATE_DEBIT_SWITCH = (
        AppiumBy.IOS_PREDICATE,
        "type == 'XCUIElementTypeSwitch'"
    )

    IOS_SUBMIT_BUTTON = (
        AppiumBy.IOS_PREDICATE,
        "type == 'XCUIElementTypeButton' AND name == 'Submit'"
    )

    # ===============================
    # ACTION METHODS
    # ===============================

    def select_account(self):
        if "ios" in self.platform:
            element = self.driver.find_element(*self.IOS_ACCOUNT_PICKER)
        else:
            element = self.driver.find_element(*self.ANDROID_ACCOUNT_PICKER)
        element.click()

    def enter_transaction_description(self, description):
        if "ios" in self.platform:
            element = self.driver.find_element(*self.IOS_TRANSACTION_DESC_FIELD)
        else:
            element = self.driver.find_element(*self.ANDROID_TRANSACTION_DESC_FIELD)
        element.clear()
        element.send_keys(description)

    def enter_transaction_amount(self, amount):
        if "ios" in self.platform:
            element = self.driver.find_element(*self.IOS_TRANSACTION_AMOUNT_FIELD)
        else:
            element = self.driver.find_element(*self.ANDROID_TRANSACTION_AMOUNT_FIELD)
        element.clear()
        element.send_keys(str(amount))

    def toggle_create_debit(self):
        if "ios" in self.platform:
            element = self.driver.find_element(*self.IOS_CREATE_DEBIT_SWITCH)
        else:
            element = self.driver.find_element(*self.ANDROID_CREATE_DEBIT_SWITCH)
        element.click()

    def click_submit(self):
        if "ios" in self.platform:
            element = self.driver.find_element(*self.IOS_SUBMIT_BUTTON)
        else:
            element = self.driver.find_element(*self.ANDROID_SUBMIT_BUTTON)
        element.click()
