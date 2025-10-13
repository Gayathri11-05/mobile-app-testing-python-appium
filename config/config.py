"""Configuration management for test automation framework."""

import os
from enum import Enum

class Platform(Enum):
    """Supported mobile platforms."""

    ANDROID = "android"
    IOS = "ios"


class Config:
    """
    Central configuration class for framework settings. This class manages all configuration parameters including
    platform settings, timeouts, and application details.
    """

    # Appium Server Configuration
    # Appium Server Configuration
    # Appium Server Configuration
    APPIUM_SERVER_URL = os.getenv(
        "APPIUM_SERVER_URL",
        f"https://{os.getenv('PERFECTO_CLOUD_NAME', 'trial')}.perfectomobile.com/nexperience/perfectomobile/wd/hub"
    )

    # Platform Selection
    PLATFORM = os.getenv("PLATFORM", Platform.ANDROID.value)

    # Timeout Configuration
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "120"))

    # Application Configuration
    ANDROID_APP_PACKAGE = os.getenv("xyz.digitalbank.demo", "")
    ANDROID_APP_ACTIVITY = os.getenv("xyz.digitalbank.demo.MainActivity", "")
    IOS_BUNDLE_ID = os.getenv("IOS_BUNDLE_ID", "")

    # ---------------------update the above details---------------------

    # Device Configuration
    ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
    ANDROID_PLATFORM_VERSION = os.getenv("ANDROID_PLATFORM_VERSION", "13.0")

    IOS_DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "iPhone 14")
    IOS_PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "16.0")

    # Test Data
    TEST_USERNAME = os.getenv("TEST_USERNAME", "bob@example.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "10203040")

    PERFECTO_CLOUD_NAME = os.getenv("PERFECTO_CLOUD_NAME", "trial")
    PERFECTO_SECURITY_TOKEN = os.getenv("PERFECTO_SECURITY_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2ZDM2NmJiNS01NDAyLTQ4MmMtYTVhOC1kODZhODk4MDYyZjIifQ.eyJpYXQiOjE3NTk3NDg2MjMsImp0aSI6ImVhMjI1ZTY1LThjYmMtNGYxZS1iZTA2LWRjOTAzNTZjNDgwYSIsImlzcyI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsImF1ZCI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsInN1YiI6IjVlYjU0ZTNjLWJkNzMtNGJjZC05YTNjLTBhMzQzOGNjNjgyNiIsInR5cCI6Ik9mZmxpbmUiLCJhenAiOiJvZmZsaW5lLXRva2VuLWdlbmVyYXRvciIsIm5vbmNlIjoiN2Q2OWY2ZDktMGEyYS00YjQxLTg3NjgtY2Y0MzdmMTQ1MzExIiwic2Vzc2lvbl9zdGF0ZSI6IjA4YWQ5Mzc3LTBlMTAtNGYwNS05MWE4LTcxMjQzNzk1ZGRkNCIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiIwOGFkOTM3Ny0wZTEwLTRmMDUtOTFhOC03MTI0Mzc5NWRkZDQifQ.HYBv6-AEgzMCRNOx8bWRkJrsaKObRBAU5QJ9p3rWYPM")

    # Reset configurations

    ANDROID_NO_RESET = os.getenv("ANDROID_NO_RESET", "false").lower() == "true"
    ANDROID_FULL_RESET = os.getenv("ANDROID_FULL_RESET", "false").lower() == "true"
    IOS_NO_RESET = os.getenv("IOS_NO_RESET", "false").lower() == "true"
    IOS_FULL_RESET = os.getenv("IOS_FULL_RESET", "false").lower() == "true"

    # Reporting Configuration
    REPORTS_DIR = "reports"
    LOGS_DIR = "logs"
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")

    @classmethod
    def get_platform(cls):
        """
        Get the current platform.

        Returns:
            Platform: The current platform enum value
        """
        return Platform(cls.PLATFORM.lower())

    @classmethod
    def is_android(cls):
        """
        Check if current platform is Android.

        Returns:
            bool: True if platform is Android, False otherwise
        """
        return cls.get_platform() == Platform.ANDROID

    @classmethod
    def is_ios(cls):
        """
        Check if current platform is iOS.

        Returns:
            bool: True if platform is iOS, False otherwise
        """
        return cls.get_platform() == Platform.IOS