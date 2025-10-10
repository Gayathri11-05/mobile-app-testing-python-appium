class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.platform = driver.capabilities.get("platformName", "").lower()
        self.logger = None  # Or set up actual logging
        self.actions = None  # Placeholder for action helper

    def get_locator(self, android_locator, ios_locator):
        """
        Returns the appropriate locator tuple based on the platform.
        """
        if "android" in self.platform:
            return android_locator
        elif "ios" in self.platform:
            return ios_locator
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")

    def wait_for_page_load(self, locator, timeout=None):
        """
        Wait for page to load by waiting for specific element.

        Args:
            locator (tuple): Locator of element indicating page loaded
            timeout (int, optional): Custom timeout in seconds

        Returns:
            bool: True if page loaded, False otherwise
        """
        element = self.actions.wait_for_element(locator, timeout)
        return element is not None

    def is_android(self):
        return self.driver.capabilities.get("platformName", "").lower() == "android"

    def is_element_visible(self, locator) -> bool:
        """
        Check if an element is visible on the page.

        Args:
            locator (tuple): The locator (By, value) for the element.

        Returns:
            bool: True if visible, False otherwise.
        """
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception:

            # except (NoSuchElementException, WebDriverException):
            # return False

            return False
