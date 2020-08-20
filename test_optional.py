import unittest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities={
        'browserName': 'Chrome',
        'platformName': 'Android',
        'platformVersion': '9.0',
        'deviceName': 'Pixel 2',
        'noReset': 'True'
    })


class test_optional(unittest.TestCase):
    def test_launch(self):
        assert driver
    def test_search(self): #TODO: perform Google search and assert plot under description element
        driver.get("https://google.com")
        driver.find_element_by_id("TODO: put search id here").send_keys("Tenet Movie Warner Brothers")
        # get plot element
        plot = "dummy"
        assert plot == "Tenet is an upcoming spy film written, produced, and directed by Christopher Nolan. It is a co-production between the United Kingdom and United States, and stars John David Washington, Robert Pattinson, Elizabeth Debicki, Dimple Kapadia, Michael Caine, and Kenneth Branagh."
