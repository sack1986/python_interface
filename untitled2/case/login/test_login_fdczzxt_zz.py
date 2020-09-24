
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
        self.allcookies = driver.get_cookies()  # 获取浏览器cookies

        #print('allcookies',allcookies)
        #mycookies = allcookies[0]['value']
        #print('mycookies', mycookies)

        # 把抓取的cookies添加到s中
        #c={'Cookie':'JSESSIONID='+mycookies}

        # 调用添加cookies函数


    def tearDown(self):
        print("test case end")



    def add_cookies(self,allcook):
        '''往session添加cookies'''
        self.sessionRequest = requests.session()
        try:
            # 添加cookies到CookieJar
            c = requests.cookies.RequestsCookieJar()
            for i in allcook:
                c.set(i["name"], i['value'])

            self.sessionRequest.cookies.update(c)  # 更新session里cookies
        except Exception as msg:
            print(u"添加cookies的时候报错了：%s" % str(msg))

        # 调用添加cookies函数


    def test_login_zz(self):
        TestLoginZZ.add_cookies(self,self.allcookies)
        print("打印s里面是否添加成功了")
        print(self.sessionRequest.cookies)

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
            #'Cookie':'JSESSIONID=69DDFCED2F9F241A43E41D62CB43F771'
        }

        response = self.sessionRequest.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

if __name__ == '__main__':
    unittest.main()