import os
from appium import webdriver
import time
import numpy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        SSID = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.ubnt.usurvey:id/vCellWifiListSsid")))
        if SSID:
            SpeedTest = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.ubnt.usurvey:id/mHomeSpeedtest")))
            SpeedTest.click()
            StartTest = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.ubnt.usurvey:id/vSpeedTestBoardStartTest")))
            StartTest.click()
            keepTesting = True
            while keepTesting:
                self.driver.implicitly_wait(60)
                TestAgain = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((
                        MobileBy.ID, "com.ubnt.usurvey:id/vSpeedTestActionTestAgain")))
                name = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((
                        MobileBy.ID, "com.ubnt.usurvey:id/vToolbarTitle"))).text
                dlSpeed = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((
                        MobileBy.ID, "com.ubnt.usurvey:id/vSpeedTestDownloadSpeedFinal"))).text
                upSpeed = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((
                        MobileBy.ID, "com.ubnt.usurvey:id/vSpeedTestUploadSpeedFinal"))).text
                print("Connection: " + name + " / Download Speed: " + dlSpeed + ", Upload Speed: " + upSpeed)
                TestAgain.click()
                assert True
                keepTesting = False # stopped testing here after proving tests can run 1 minute apart

        else:
            print("No SSID found")
            assert False
        # self.driver.click(TODO: find id of SSID if available, or exit if none found
        # self.driver.click(TODO: find id of Speed Test -> Start Test soft button)
        # print(status depending on if SSID was found or not)
        return True

    def tearDown(self):
        self.driver.quit()
