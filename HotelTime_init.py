import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
 
class TableSearchTest(unittest.TestCase):
 
    def setUp(self):
        # Kakao Game SDK Test App 경로
        app = os.path.join(os.path.dirname(__file__), '/Users/jun.k/apk',
                           'hotelTime_70_appCenter_debug.apk')
        app = os.path.abspath(app)
 
        # Set up appium
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '9.0',
                'deviceName': 'Galaxy S8',
                'automationName': 'Appium',
                'appPackage': 'com.withweb.hoteltime',
                'appActivity': 'com.withweb.hoteltime.pages.splash.SplashActivity',
                'udid': 'ce031713a8824d0f05'
            })
 
    def test_search_field(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
 
        window_size = driver.get_window_size()
        max_width = int(window_size["width"] * 0.70)
        max_height = int(window_size["height"] * 0.30)
 
        sleep(3)
 
        standby_server = driver.find_element_by_xpath("//android.widget.TextView[@index='1']").click()
        driver.implicitly_wait(5)
        permission_allow = driver.find_element_by_xpath("//android.widget.Button[@index='1']").click()
        driver.implicitly_wait(5)
        permission_allow = driver.find_element_by_xpath("//android.widget.Button[@index='1']").click()
 
        for row in range(2):
            sleep(3)
            driver.swipe(max_width, int(max_height/2), 0, int(max_height), 500)
 
        driver.implicitly_wait(5)
        later_select = driver.find_element_by_id("tv_goto_main").click()
 
        sleep(3)
 
        try:
            popup = driver.find_element_by_id("iv_banner").is_enabled()
            close_button = driver.find_element_by_id("tv_left_action").click()
            sleep(3)
        except:
            sleep(3)
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TableSearchTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
