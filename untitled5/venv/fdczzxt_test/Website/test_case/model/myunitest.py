import unittest
from selenium import webdriver
from driver.driver import *


class StarEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(3)
        # self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


