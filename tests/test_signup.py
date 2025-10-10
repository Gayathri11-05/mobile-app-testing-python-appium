import pytest
from pages.sign_up import SignupPage

@pytest.mark.usefixtures("driver_setup")
class TestSignup:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.signup_page = SignupPage(driver)

    def test_successful_registration(self):
        """Verify user can register successfully with valid data."""
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "ssn": "123-45-6789",
            "email": "john.doe@example.com",
            "password": "Secure@123",
            "address": "123 Elm Street",
            "region": "California",
            "locality": "San Jose",
            "postcode": "95123",
            "country": "USA",
            "home_phone": "1234567890",
            "mobile_phone": "9876543210",
            "work_phone": "1112223333",
        }

        result = self.signup_page.register_new_user(user_data)
        assert result, "User registration failed when it should have succeeded."

    def test_registration_missing_fields(self):
        """Verify registration fails when mandatory fields are missing."""
        incomplete_data = {
            "first_name": "",
            "last_name": "",
            "ssn": "",
            "email": "",
            "password": "",
            "address": "",
            "region": "",
            "postcode": "",
            "country": "",
            "home_phone": "",
            "mobile_phone": "",
            "work_phone": "",
        }

        result = self.signup_page.register_new_user(incomplete_data)
        assert not result, "Registration should fail for missing mandatory fields."
        assert self.signup_page.is_error_displayed(), "Error message not shown for invalid signup."

    def test_invalid_email_format(self):
        """Verify that invalid email format is not accepted."""
        user_data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "ssn": "321-54-9876",
            "email": "invalid_email",
            "password": "ValidPass@1",
            "address": "456 Oak Avenue",
            "region": "Texas",
            "locality": "Austin",
            "postcode": "73301",
            "country": "USA",
            "home_phone": "1234567890",
            "mobile_phone": "9876543210",
            "work_phone": "1112223333",
        }

        result = self.signup_page.register_new_user(user_data)
        assert not result, "Registration should fail for invalid email format."
        error_text = self.signup_page.get_error_message()
        assert "Invalid" in error_text or "Email" in error_text, f"Unexpected error: {error_text}"

    def test_registration_without_accepting_terms(self):
        """Verify that registration fails when user does not accept terms."""
        user_data = {
            "first_name": "Robert",
            "last_name": "Brown",
            "ssn": "123-11-2222",
            "email": "robert.brown@example.com",
            "password": "Valid@123",
            "address": "789 Maple Drive",
            "region": "Florida",
            "locality": "Miami",
            "postcode": "33101",
            "country": "USA",
            "home_phone": "1234567890",
            "mobile_phone": "9876543210",
            "work_phone": "1112223333",
        }

        # Intentionally skip accept_terms
        self.signup_page.enter_first_name(user_data["first_name"])
        self.signup_page.enter_last_name(user_data["last_name"])
        self.signup_page.select_gender_male()
        self.signup_page.set_date_of_birth()
        self.signup_page.enter_ssn(user_data["ssn"])
        self.signup_page.enter_email(user_data["email"])
        self.signup_page.enter_password(user_data["password"])
        self.signup_page.enter_address(user_data["address"])
        self.signup_page.enter_region(user_data["region"])
        self.signup_page.enter_locality(user_data["locality"])
        self.signup_page.enter_postcode(user_data["postcode"])
        self.signup_page.enter_country(user_data["country"])
        self.signup_page.enter_home_phone(user_data["home_phone"])
        self.signup_page.enter_mobile_phone(user_data["mobile_phone"])
        self.signup_page.enter_work_phone(user_data["work_phone"])
        self.signup_page.click_register_button()

        assert self.signup_page.is_error_displayed(), "Error should appear when terms are not accepted."

