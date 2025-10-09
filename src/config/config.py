"""Configuration management for Digital Banking app test automation framework."""

import os
from enum import Enum


class Platform(Enum):
    """Supported mobile platforms."""
    ANDROID = "android"
    IOS = "ios"


class Config:
    """
    Central configuration class for framework settings.

    Manages platform, device, app, test data, timeouts, and reporting.
    """

    # Perfecto / Appium Server
    APPIUM_SERVER_URL = os.getenv(
        "APPIUM_SERVER_URL",
        "https://trial.perfectomobile.com/nexperience/perfectomobile/wd/hub"
    )

    # Platform selection
    PLATFORM = os.getenv("PLATFORM", Platform.ANDROID.value)

    # Timeout settings
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "3600"))

    # Android App & Device
    ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "37271FDJH008ER")
    ANDROID_PLATFORM_VERSION = os.getenv("ANDROID_PLATFORM_VERSION", "16")
    ANDROID_APP_PACKAGE = "xyz.digitalbank.demo"
    ANDROID_APP_ACTIVITY = "xyz.digitalbank.demo.MainActivity"
    ANDROID_NO_RESET = True  # Keep app state between sessions

    # iOS App & Device
    IOS_DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "00008110-000951DE34A2801E")
    IOS_PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "17.3")
    IOS_BUNDLE_ID = "demoddbank.perforce.com"
    IOS_NO_RESET = True  # Keep app state between sessions

    # Test Credentials (placeholders, update as needed)
    TEST_USERNAME = os.getenv("TEST_USERNAME", "testuser@example.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "Password123")
    TEST_ACCOUNT_NUMBER = os.getenv("TEST_ACCOUNT_NUMBER", "12345678")
    TEST_PIN = os.getenv("TEST_PIN", "1234")

    # Reporting
    REPORTS_DIR = "reports"
    LOGS_DIR = "logs"
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")

    @classmethod
    def get_platform(cls):
        return Platform(cls.PLATFORM.lower())

    @classmethod
    def is_android(cls):
        return cls.get_platform() == Platform.ANDROID

    @classmethod
    def is_ios(cls):
        return cls.get_platform() == Platform.IOS
