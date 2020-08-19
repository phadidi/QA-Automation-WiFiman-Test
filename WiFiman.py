import os
from appium import webdriver
import time


class WiFiman:
    def __init__(self):
        app = os.path.abspath(
            'C:\\Users\\hadidip\\AndroidStudioProjects\\QAAutomationInterviewChallenge\\app\\build\\outputs\\apk'
            '\\debug\\WiFiman Find nearby WiFi APs and run speed test_v1.5.2_apkpure.com.apk')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '9.0',
                'deviceName': 'Pixel 2',
                'noReset': 'True'
            }
        )

    def getSpeedPerMinute(self):
        SSID = self.driver.find_element_by_android_uiautomator('new UiSelector().text("AndroidWifi")')

    # if (SSID): self.driver.implicitly_wait(60) SpeedTest = self.driver.find_element_by_android_uiautomator(
    # '//android.widget.FrameLayout[@content-desc="Speed Test"]') SpeedTest()

    def tearDown(self):
        self.driver.quit()
