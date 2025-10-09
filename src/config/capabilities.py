"""Device capabilities configuration for Digital Banking app (Android & iOS)."""
import os
from ..config.config import Config


class Capabilities:
    """
    Provides device-specific capabilities for Appium / Perfecto.
    """

    @staticmethod
    def get_android_capabilities():
        return {
            "platformName": "Android",
            "platformVersion": Config.ANDROID_PLATFORM_VERSION,
            "deviceName": Config.ANDROID_DEVICE_NAME,
            "automationName": "UiAutomator2",
            "appPackage": Config.ANDROID_APP_PACKAGE,
            "appActivity": Config.ANDROID_APP_ACTIVITY,
            "noReset": Config.ANDROID_NO_RESET,
            "newCommandTimeout": Config.COMMAND_TIMEOUT,
            "orientation": "PORTRAIT",
            "language": "en",
            "locale": "US",
            # Perfecto-specific options (optional)
            "securityToken": os.getenv("PERFECTO_SECURITY_TOKEN", ""),
        }

    @staticmethod
    def get_ios_capabilities():
        return {
            "platformName": "iOS",
            "platformVersion": Config.IOS_PLATFORM_VERSION,
            "deviceName": Config.IOS_DEVICE_NAME,
            "automationName": "XCUITest",
            "bundleId": Config.IOS_BUNDLE_ID,
            "noReset": Config.IOS_NO_RESET,
            "newCommandTimeout": Config.COMMAND_TIMEOUT,
            "orientation": "PORTRAIT",
            "language": "en",
            "locale": "US",
            "autoAcceptAlerts": True,
            # Perfecto-specific options (optional)
            "securityToken": os.getenv("PERFECTO_SECURITY_TOKEN", ""),
        }

    @staticmethod
    def get_capabilities():
        if Config.is_android():
            return Capabilities.get_android_capabilities()
        else:
            return Capabilities.get_ios_capabilities()
