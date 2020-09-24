
import unittest
import requests
from selenium import webdriver
import time
import json

class TestLoginZZ(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 静默模式
        driver = webdriver.Chrome(chrome_options=option)
        url = 'http://192.168.0.236:8180/fdczzxt/login'
        driver.get(url)
        # 先登录
        time.sleep(3)
        driver.find_element_by_id("j_username").send_keys("dlzzjj")
        driver.find_element_by_id("j_password1").send_keys("a1234567")
        driver.find_element_by_id("loginclick").click()

        time.sleep(3)
        allcookies = driver.get_cookies()  # 获取浏览器cookies

        #获取value值
        self.mycookies = allcookies[0]['value']


    def tearDown(self):
        print("test case end")


    def test_login_zz(self):

        url = "http://192.168.0.236:8180/fdczzxt/j_spring_security_check"

        payload = "j_username=dhzzjj&j_password=5690dddfa28ae085d23518a035707282"
        headers = {
            'Accept':'text/html,application/xhtml+xml, image/jxr,*/*',
            'Referer':'http://192.168.0.236:8180/fdczzxt/login',
            'Accept-Language':'zh - CN',
            'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64;Trident/7.0;rv: 11.0)likeGecko',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept-Encoding':'gzip, deflate',
            'Host':'192.168.0.236:8180',
            'Connection':'Keep-Alive',
            'Pragma':'no-cache',
            'Cookie':'JSESSIONID='+self.mycookies
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

if __name__ == '__main__':
    unittest.main()