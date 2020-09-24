from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os



class Page():
    """页面基础类"""

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://192.168.0.236:8180/fdczzxt/login'
        self.timeout = 10

    # 打开不同的子页面
    def _open(self):
        url_ = self.base_url
        print("Test page is %s" % url_)
        #self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        #assert self.driver.current_url == url_, 'Did not land on %s' % url_

    def open(self):
        self._open()

    # 元素定位封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)
    # 下拉框
    def select_element(self,s,textinfo):
        return Select(s).select_by_visible_value(textinfo)
    #切换iframe
    def switch_iframe(self,iframe):
        self.driver.switch_to_frame(iframe)
    #释放iframe
    def default_iframe(self):
        self.driver.switch_to_default_content()
    # def find_alert(self):
    #     return self.driver.switch_to_alert()

    # def find_element(self, *loc):
    #     Actions action = new Actions(driver)
    #     action.doubleclick(*loc).perform;


