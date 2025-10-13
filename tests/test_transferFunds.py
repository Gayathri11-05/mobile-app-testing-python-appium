import pytest
from pages.transferFunds import DepositPage


@pytest.mark.deposit
class TestDeposit:

    @pytest.mark.android
    def test_make_deposit_android(self, driver):
        """Test deposit flow on Android."""
        deposit_page = DepositPage(driver)

        # Perform actions
        deposit_page.select_account()
        deposit_page.enter_transaction_description("Salary Deposit")
        deposit_page.enter_transaction_amount(5000)
        deposit_page.toggle_create_debit()
        deposit_page.click_submit()

        # Example assertion (you can adjust to your app)
        # Ideally, verify success toast or navigation
        success_toast = driver.find_element_by_xpath(
            "//*[@text='Transaction successful' or contains(@content-desc, 'Transaction successful')]"
        )
        assert success_toast.is_displayed(), "Transaction success toast not visible."

    @pytest.mark.ios
    def test_make_deposit_ios(self, driver):
        """Test deposit flow on iOS."""
        deposit_page = DepositPage(driver)

        # Perform actions
        deposit_page.select_account()
        deposit_page.enter_transaction_description("Salary Deposit")
        deposit_page.enter_transaction_amount(5000)
        deposit_page.toggle_create_debit()
        deposit_page.click_submit()

        # Example assertion (customize for your app)
        success_alert = driver.find_element_by_ios_predicate(
            "type == 'XCUIElementTypeStaticText' AND name == 'Transaction successful'"
        )
        assert success_alert.is_displayed(), "Success alert not visible on iOS."
