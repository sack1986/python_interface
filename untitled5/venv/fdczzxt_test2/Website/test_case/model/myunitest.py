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

    driver = None


    # def setUp(self):
    #     print('start')
    #     if self.driver is None:
    #         self.driver == browser()
    #
    #
    # def tearDown(self):
    #     print('end')
    #     if self.driver:
    #         self.driver.quit()
    #     self.driver = None


