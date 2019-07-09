import unittest
from selenium import webdriver
import time

path = '/home/jatin/Downloads/chromedriver'


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()

    def test_frame(self):
        driver = self.driver
        driver.get('https://www.toolsqa.com/iframe-practice-page/')
        driver.execute_script('window.scrollTo(0, 620)')
        time.sleep(5)

# Switching to 1st Frame
        iframe1 = driver.find_element_by_id('IF1')
        driver.switch_to.frame(iframe1)

# Scrolling the page
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(4)

        driver.switch_to_default_content()

# Switching to 2nd Frame
        iframe2 = driver.find_element_by_id('IF2')
        driver.switch_to_frame(iframe2)

# Click on Resizable
        driver.find_element_by_xpath('//*[@id="sidebar"]/aside[1]/ul/li[3]/a').click()
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
