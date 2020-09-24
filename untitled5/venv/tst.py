import unittest
import time
from selenium import webdriver



class SearchTest(unittest.TestCase):
#class SearchTest():

    @classmethod
    def setUpClass(cls) :
        # webdriver.Ie("D:\Python36\IEDriverServer.exe")
        cls.driver=webdriver.Ie()
        # webdriver.chrome()
        # driver.maximize_window()
        # driver.implicitly_wait(8)
        cls.driver.get("https://www.baidu.com")

    def test_myCase1(self):
        baidu1= self.driver.find_element_by_id("kw")
        baidu1.clear()
        baidu1.send_keys("测试1")
        bat1 = self.driver.find_element_by_id("su")
        bat1.submit()

    def test_myCase2(self):
        baidu2=self.driver.find_element_by_id("kw")
        baidu2.clear()
        baidu2.send_keys("测试2")
        bat2 = self.driver.find_element_by_id("su")
        bat2.submit()

    @classmethod
    def tearDownClass(cls) :
        time.sleep(5)
        cls.driver.quit()



if __name__ == "__main__":
    #unittest.main()
    #SearchTest.test_myCase(self)


    # mySuite=unittest.TestSuite()
    # mySuite.addTest(SearchTest("test_myCase1"))
    # mySuite.addTest(SearchTest("test_myCase2"))
    # myRunner=unittest.TextTestRunner()
    # myRunner.run(mySuite)



