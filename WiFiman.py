import os
from appium import webdriver
import time
import numpy


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

    def getSpeed(self):
        # self.driver.click(TODO: find id of SSID if available, or exit if none found
        # self.driver.click(TODO: find id of Speed Test -> Start Test soft button)
        # print(status depending on if SSID was found or not)
        return True

    def tearDown(self):
        self.driver.quit()
