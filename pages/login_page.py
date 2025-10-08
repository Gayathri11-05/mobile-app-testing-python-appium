"""Login page object."""

from appium.webdriver.common.appiumby import AppiumBy as By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Login page object for Digital Bank App.

    Contains all locators and methods related to login functionality.
    """

    # Android Locators
    ANDROID_EMAIL_FIELD = (
        By.ID,
        "xyz.digitalbank.demo:id/emailInput"
    )
    ANDROID_PASSWORD_FIELD = (
        By.ID,
        "xyz.digitalbank.demo:id/passwordInput"
    )
    ANDROID_LOGIN_BUTTON = (
        By.ID,
        "xyz.digitalbank.demo:id/login"
    )
    ANDROID_SIGNUP_LINK = (
        By.ID,
        "xyz.digitalbank.demo:id/registerTV"
    )

    # iOS Locators
    IOS_EMAIL_FIELD = (
        By.IOS_PREDICATE,
        "value == 'jsmith@demo.io' OR name == 'email'"
    )
    IOS_PASSWORD_FIELD = (
        By.IOS_PREDICATE,
        "type == 'XCUIElementTypeSecureTextField' OR name == 'password'"
    )
    IOS_LOGIN_BUTTON = (
        By.ACCESSIBILITY_ID,
        "LogIn"
    )
    IOS_SIGNUP_LINK = (
        By.ACCESSIBILITY_ID,
        "Sign Up Here"
    )

    def __init__(self, driver):
        """
        Initialize LoginPage.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        super().__init__(driver)

    def enter_email(self, email):
        """
        Enter email address in the email field.

        Args:
            email (str): Email address to enter

        Returns:
            bool: True if successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_EMAIL_FIELD,
            self.IOS_EMAIL_FIELD
        )
        success = self.actions.send_keys(locator, email)
        if success:
            self.logger.info(f"Entered email: {email}")
        return success

    def enter_password(self, password):
        """
        Enter password in the password field.

        Args:
            password (str): Password to enter

        Returns:
            bool: True if successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_PASSWORD_FIELD,
            self.IOS_PASSWORD_FIELD
        )
        success = self.actions.send_keys(locator, password)
        if success:
            self.logger.info("Entered password")
        return success

    def click_login_button(self):
        """
        Click the login button.

        Returns:
            bool: True if successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_LOGIN_BUTTON,
            self.IOS_LOGIN_BUTTON
        )
        success = self.actions.click(locator)
        if success:
            self.logger.info("Clicked Login button")
        return success

    def click_signup_link(self):
        """
        Click the 'Sign Up Here' link.

        Returns:
            bool: True if successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_SIGNUP_LINK,
            self.IOS_SIGNUP_LINK
        )
        success = self.actions.click(locator)
        if success:
            self.logger.info("Clicked Sign Up link")
        return success

    def login(self, email, password):
        """
        Perform complete login flow.

        Args:
            email (str): Email address to login with
            password (str): Password to login with

        Returns:
            bool: True if login successful, False otherwise
        """
        self.logger.info(f"Attempting login with email: {email}")

        if not self.enter_email(email):
            return False

        if not self.enter_password(password):
            return False

        if not self.click_login_button():
            return False

        self.actions.hide_keyboard()
        self.logger.info("Login flow completed")
        return True
