"""Signup page object."""

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SignupPage(BasePage):
    """
    Signup (Registration) page object for My Demo App.

    Contains all locators and methods related to user registration functionality,
    including success and error validations.
    """

    # ----------------------------
    # Android Locators
    # ----------------------------

    ANDROID_FIRST_NAME_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter First Name"
    )
    ANDROID_LAST_NAME_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Last Name"
    )
    ANDROID_GENDER_MALE = (
        AppiumBy.ACCESSIBILITY_ID, "Select Male Gender"
    )
    ANDROID_GENDER_FEMALE = (
        AppiumBy.ACCESSIBILITY_ID, "Select Female Gender"
    )
    ANDROID_DOB_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Date of Birth"
    )
    ANDROID_YEAR_PICKER = (
        AppiumBy.ID, "android:id/date_picker_header_year"
    )
    ANDROID_YEAR_2023 = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2023")'
    )
    ANDROID_DOB_OK_BUTTON = (
        AppiumBy.ID, "android:id/button1"
    )
    ANDROID_SSN_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Social Security Number"
    )
    ANDROID_EMAIL_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Email Address"
    )
    ANDROID_PASSWORD_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Password"
    )
    ANDROID_ADDRESS_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Address"
    )
    ANDROID_REGION_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Region"
    )
    ANDROID_LOCALITY_FIELD = (
        AppiumBy.ID, "xyz.digitalbank.demo:id/localityInput"
    )
    ANDROID_POSTCODE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter PostCode"
    )
    ANDROID_COUNTRY_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Country"
    )
    ANDROID_HOME_PHONE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Home Phone"
    )
    ANDROID_MOBILE_PHONE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Mobile Phone"
    )
    ANDROID_WORK_PHONE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Work Phone"
    )
    ANDROID_TERMS_CHECKBOX = (
        AppiumBy.ACCESSIBILITY_ID, "Accept Terms and Conditions"
    )
    ANDROID_REGISTER_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID, "Register Button"
    )
    ANDROID_CONFIRM_OK_BUTTON = (
        AppiumBy.ID, "android:id/button1"
    )

    # Validation / Alerts
    ANDROID_SUCCESS_MESSAGE = (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text, 'Registration Successful')]"
    )
    ANDROID_ERROR_MESSAGE = (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text, 'Error') or contains(@text, 'Failed')]"
    )

    # ----------------------------
    # iOS Locators
    # ----------------------------

    IOS_FIRST_NAME_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter First Name"
    )
    IOS_LAST_NAME_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Last Name"
    )
    IOS_GENDER_MALE = (
        AppiumBy.ACCESSIBILITY_ID, "Select Male Gender"
    )
    IOS_GENDER_FEMALE = (
        AppiumBy.ACCESSIBILITY_ID, "Select Female Gender"
    )
    IOS_DOB_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Date of Birth"
    )
    IOS_SSN_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Social Security Number"
    )
    IOS_EMAIL_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Email Address"
    )
    IOS_PASSWORD_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Password"
    )
    IOS_ADDRESS_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Address"
    )
    IOS_REGION_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Region"
    )
    IOS_POSTCODE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter PostCode"
    )
    IOS_COUNTRY_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Country"
    )
    IOS_HOME_PHONE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Home Phone"
    )
    IOS_MOBILE_PHONE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Mobile Phone"
    )
    IOS_WORK_PHONE_FIELD = (
        AppiumBy.ACCESSIBILITY_ID, "Enter Work Phone"
    )
    IOS_TERMS_CHECKBOX = (
        AppiumBy.ACCESSIBILITY_ID, "Accept Terms and Conditions"
    )
    IOS_REGISTER_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID, "Register Button"
    )
    IOS_CONFIRM_OK_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID, "OK"
    )

    # Validation / Alerts
    IOS_SUCCESS_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Registration Successful")
    IOS_ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Error Alert")

    def __init__(self, driver):
        super().__init__(driver)

    # ----------------------------
    # Field Interaction Methods
    # ----------------------------
    def enter_first_name(self, first_name):
        locator = self.get_locator(self.ANDROID_FIRST_NAME_FIELD, self.IOS_FIRST_NAME_FIELD)
        return self.actions.send_keys(locator, first_name)

    def enter_last_name(self, last_name):
        locator = self.get_locator(self.ANDROID_LAST_NAME_FIELD, self.IOS_LAST_NAME_FIELD)
        return self.actions.send_keys(locator, last_name)

    def select_gender_male(self):
        locator = self.get_locator(self.ANDROID_GENDER_MALE, self.IOS_GENDER_MALE)
        return self.actions.click(locator)

    def set_date_of_birth(self,):
        dob_locator = self.get_locator(self.ANDROID_DOB_FIELD, self.IOS_DOB_FIELD)
        self.actions.click(dob_locator)
        if self.is_android():
            self.actions.click(self.ANDROID_YEAR_PICKER)
            self.actions.click(self.ANDROID_YEAR_2023)
            self.actions.click(self.ANDROID_DOB_OK_BUTTON)
        return True

    def enter_ssn(self, ssn):
        locator = self.get_locator(self.ANDROID_SSN_FIELD, self.IOS_SSN_FIELD)
        return self.actions.send_keys(locator, ssn)

    def enter_email(self, email):
        locator = self.get_locator(self.ANDROID_EMAIL_FIELD, self.IOS_EMAIL_FIELD)
        return self.actions.send_keys(locator, email)

    def enter_password(self, password):
        locator = self.get_locator(self.ANDROID_PASSWORD_FIELD, self.IOS_PASSWORD_FIELD)
        return self.actions.send_keys(locator, password)

    def enter_address(self, address):
        locator = self.get_locator(self.ANDROID_ADDRESS_FIELD, self.IOS_ADDRESS_FIELD)
        return self.actions.send_keys(locator, address)

    def enter_region(self, region):
        locator = self.get_locator(self.ANDROID_REGION_FIELD, self.IOS_REGION_FIELD)
        return self.actions.send_keys(locator, region)

    def enter_locality(self, locality):
        if self.is_android():
            return self.actions.send_keys(self.ANDROID_LOCALITY_FIELD, locality)
        return False

    def enter_postcode(self, postcode):
        locator = self.get_locator(self.ANDROID_POSTCODE_FIELD, self.IOS_POSTCODE_FIELD)
        return self.actions.send_keys(locator, postcode)

    def enter_country(self, country):
        locator = self.get_locator(self.ANDROID_COUNTRY_FIELD, self.IOS_COUNTRY_FIELD)
        return self.actions.send_keys(locator, country)

    def enter_home_phone(self, number):
        locator = self.get_locator(self.ANDROID_HOME_PHONE_FIELD, self.IOS_HOME_PHONE_FIELD)
        return self.actions.send_keys(locator, number)

    def enter_mobile_phone(self, number):
        locator = self.get_locator(self.ANDROID_MOBILE_PHONE_FIELD, self.IOS_MOBILE_PHONE_FIELD)
        return self.actions.send_keys(locator, number)

    def enter_work_phone(self, number):
        locator = self.get_locator(self.ANDROID_WORK_PHONE_FIELD, self.IOS_WORK_PHONE_FIELD)
        return self.actions.send_keys(locator, number)

    def accept_terms(self):
        locator = self.get_locator(self.ANDROID_TERMS_CHECKBOX, self.IOS_TERMS_CHECKBOX)
        return self.actions.click(locator)

    def click_register_button(self):
        locator = self.get_locator(self.ANDROID_REGISTER_BUTTON, self.IOS_REGISTER_BUTTON)
        return self.actions.click(locator)

    # ----------------------------
    # Validation Helpers
    # ----------------------------
    def is_error_displayed(self):
        locator = self.get_locator(self.ANDROID_ERROR_MESSAGE, self.IOS_ERROR_MESSAGE)
        return self.actions.is_displayed(locator, timeout=5)

    def get_error_message(self):
        locator = self.get_locator(self.ANDROID_ERROR_MESSAGE, self.IOS_ERROR_MESSAGE)
        return self.actions.get_text(locator)

    def is_success_displayed(self):
        locator = self.get_locator(self.ANDROID_SUCCESS_MESSAGE, self.IOS_SUCCESS_MESSAGE)
        return self.actions.is_displayed(locator, timeout=8)

    # ----------------------------
    # High-level flow
    # ----------------------------
    def register_new_user(self, user_data):
        """
        Perform complete signup (registration) flow with validation.

        Args:
            user_data (dict): User registration details.

        Returns:
            bool: True if registration successful, False otherwise.
        """
        self.logger.info(f"Registering user: {user_data.get('email')}")

        try:
            self.enter_first_name(user_data["first_name"])
            self.enter_last_name(user_data["last_name"])
            self.select_gender_male()
            self.set_date_of_birth()
            self.enter_ssn(user_data["ssn"])
            self.enter_email(user_data["email"])
            self.enter_password(user_data["password"])
            self.enter_address(user_data["address"])
            self.enter_region(user_data["region"])
            self.enter_locality(user_data.get("locality", ""))
            self.enter_postcode(user_data["postcode"])
            self.enter_country(user_data["country"])
            self.enter_home_phone(user_data["home_phone"])
            self.enter_mobile_phone(user_data["mobile_phone"])
            self.enter_work_phone(user_data["work_phone"])
            self.accept_terms()

            if not self.click_register_button():
                self.logger.error("Failed to click Register button.")
                return False

            # Hide keyboard and wait for result
            self.actions.hide_keyboard()

            # Check for success or error message
            if self.is_success_displayed():
                self.logger.info("Registration successful!")
                return True
            elif self.is_error_displayed():
                error_msg = self.get_error_message()
                self.logger.error(f"Registration failed: {error_msg}")
                return False
            else:
                self.logger.warning("No confirmation message detected after registration.")
                return False

        except Exception as e:
            self.logger.exception(f"Exception during registration: {str(e)}")
            return False
