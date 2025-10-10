"""Configuration management for test automation framework."""

import os
from enum import Enum


class Platform(Enum):
    """Supported mobile platforms."""
    ANDROID = "android"
    IOS = "ios"


class Config:
    """
    Central configuration class for framework settings.
    Manages platform, device, app, timeout, and Perfecto credentials.
    """

    # ----------------------------
    # 🔹 Perfecto Cloud Configuration
    # ----------------------------
    PERFECTO_CLOUD_NAME = os.getenv("PERFECTO_CLOUD_NAME", "trial")  # change if not 'trial'
    PERFECTO_SECURITY_TOKEN = os.getenv("PERFECTO_SECURITY_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2ZDM2NmJiNS01NDAyLTQ4MmMtYTVhOC1kODZhODk4MDYyZjIifQ.eyJpYXQiOjE3NTk3NDQ4MTIsImp0aSI6ImUxYjQzNWQ0LTQyMTEtNGE0ZC1iZWIyLWMxNTA4MjQ2NGZkZSIsImlzcyI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsImF1ZCI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsInN1YiI6IjQwNTcwNGRmLTQ1MzMtNGQxYS1iYjc3LWExYTM1ZWRjMDM2NCIsInR5cCI6Ik9mZmxpbmUiLCJhenAiOiJvZmZsaW5lLXRva2VuLWdlbmVyYXRvciIsIm5vbmNlIjoiYmJiZWNhZmMtN2NjZS00MWJlLWJkMjQtZGY2OTVmNjlkMDVlIiwic2Vzc2lvbl9zdGF0ZSI6ImUyYmRlNmJiLWViNmQtNDFkNi04MjcyLWZlOGFiZmI0ZjQ4OCIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJlMmJkZTZiYi1lYjZkLTQxZDYtODI3Mi1mZThhYmZiNGY0ODgifQ.8EKfMAY_FB3ng7lBwG31du6huoTNAVJox5hvtpnMq2w")

    # Construct the Appium Server URL dynamically for Perfecto
    APPIUM_SERVER_URL = (
        f"https://{PERFECTO_CLOUD_NAME}.perfectomobile.com/nexperience/perfectomobile/wd/hub"
    )

    # ----------------------------
    # 🔹 Platform Selection
    # ----------------------------
    PLATFORM = os.getenv("PLATFORM", Platform.ANDROID.value)

    # ----------------------------
    # 🔹 Timeout Configuration
    # ----------------------------
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "120"))

    # ----------------------------
    # 🔹 Application Configuration
    # ----------------------------
    # Android App Details
    ANDROID_APP_PACKAGE = os.getenv("ANDROID_APP_PACKAGE", "xyz.digitalbank.demo")
    ANDROID_APP_ACTIVITY = os.getenv("ANDROID_APP_ACTIVITY", "xyz.digitalbank.demo.MainActivity")

    # iOS App Details
    IOS_BUNDLE_ID = os.getenv("IOS_BUNDLE_ID", "demoddbank.perforce.com")

    # ----------------------------
    # 🔹 Device Configuration
    # ----------------------------
    # Android Device (From Perfecto Device ID)
    ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "37271FDJH008ER")
    ANDROID_PLATFORM_VERSION = os.getenv("ANDROID_PLATFORM_VERSION", "16")

    # iOS Device (From Perfecto Device UDID)
    IOS_DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "00008110-000951DE34A2801E")
    IOS_PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "17.3")

    # ----------------------------
    # 🔹 Reporting Configuration
    # ----------------------------
    REPORTS_DIR = "reports"
    LOGS_DIR = "logs"
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")

    # ----------------------------
    # 🔹 Platform Helpers
    # ----------------------------
    @classmethod
    def get_platform(cls):
        """Get the current platform."""
        return Platform(cls.PLATFORM.lower())

    @classmethod
    def is_android(cls):
        """Check if current platform is Android."""
        return cls.get_platform() == Platform.ANDROID

    @classmethod
    def is_ios(cls):
        """Check if current platform is iOS."""
        return cls.get_platform() == Platform.IOS
