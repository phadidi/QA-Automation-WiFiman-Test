import unittest

from appium import webdriver
from selenium.webdriver.common.keys import Keys

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

    def test_search(self):
        driver.get("https://google.com")
        searchBar = driver.find_element_by_name('q')
        searchBar.send_keys("Tenet Movie Warner Brothers")
        searchBar.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        kno_rdesc = driver.find_element_by_class_name("kno-rdesc").text
        # remove "Description\n" from plot
        description = kno_rdesc.split("Description\n")
        plot = description[1]
        assert plot == "Tenet is an upcoming spy film written, produced, and directed by Christopher Nolan. It is a co-production between the United Kingdom and United States, and stars John David Washington, Robert Pattinson, Elizabeth Debicki, Dimple Kapadia, Michael Caine, and Kenneth Branagh."
