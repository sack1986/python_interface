import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait




class SearchTest(unittest.TestCase):
#class SearchTest():

    @classmethod
    def setUpClass(cls) :
        # webdriver.Ie("D:\Python36\IEDriverServer.exe")
        cls.driver=webdriver.Ie()
        # webdriver.chrome()
        # driver.maximize_window()
        # driver.implicitly_wait(8)
        cls.driver.get("http://192.168.0.249:9080/fdczzxt")

    def test_myCase(self):

        name= self.driver.find_element_by_id("j_username")
        name.clear()
        name.send_keys("昆明未来城开发有限公司")

        # '使用tab键定位元素'
        # name.send_keys(Keys.TAB)
        # actionChains =ActionChains(self.driver)
        # actionChains.send_keys('1234')
        # actionChains.perform()


        password = self.driver.find_element_by_id("j_password")
        password.clear()
        password.send_keys("1234")

        login = self.driver.find_element_by_id("loginclick")
        login.submit()
        loginName=WebDriverWait(self.driver,5).until(lambda mydriver:self.driver.find_element_by_css_selector("body.page-container-bg-solid:nth-child(2) div.page-wrapper:nth-child(1) div.page-wrapper-row:nth-child(1) div.page-wrapper-top div.page-header div.page-header-top div.container-fluid div.top-menu ul.nav.navbar-nav.pull-right li.dropdown.dropdown-user.dropdown-dark:nth-child(1) > a.dropdown-toggle"))
        self.assertEqual(loginName.text,"昆明未来城开发有限公司")

        # time.sleep(5)
        # qiye_maniu=self.driver.find_element_by_css_selector("body > div.page-wrapper > div:nth-child(1) > div > div > div.page-header-menu > div > div.hor-menu > ul > li:nth-child(2) > a")
        # qiye_maniu.click()
        #
        # time.sleep(5)
        # qiye=self.driver.find_element_by_css_selector("body.page-container-bg-solid:nth-child(2) div.page-wrapper:nth-child(1) div.page-wrapper-row.full-height:nth-child(3) div.page-wrapper-middle div.page-container div.page-content-wrapper div.page-content div.container-fluid div.home-index-oper ul:nth-child(1) li:nth-child(1) > a:nth-child(1)")
        # qiye.click()
        # time.sleep(5)





    @classmethod
    def tearDownClass(cls) :
        time.sleep(5)
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()
    SearchTest.test_myCase(self)


    # mySuite=unittest.TestSuite()
    # mySuite.addTest(SearchTest("test_myCase1"))
    # mySuite.addTest(SearchTest("test_myCase2"))
    # myRunner=unittest.TextTestRunner()
    # myRunner.run(mySuite)



