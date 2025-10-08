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
