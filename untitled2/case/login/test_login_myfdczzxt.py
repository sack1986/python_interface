# coding:utf-8

import unittest
import requests
from selenium import webdriver
import time
import re


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_login(self):

        url = "http://192.168.0.236:8180/fdczzxt/j_spring_security_check"

        payload = "j_username=测试机构&j_password=5690dddfa28ae085d23518a035707282".encode('utf-8')
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
            'Cookie':'JSESSIONID=69DDFCED2F9F241A43E41D62CB43F771'
       }

        response = requests.request("POST", url, headers=headers, data=payload)
        mytest1=response.text
        mystr1="退出系统"
        result=TestLogin.my_verify(self,mytest1,mystr1)
        return self.assertEqual(result,True)

    '正则表达式搜索指定内容'
    def my_verify(self, mytest, mystr):
        pattern=re.compile(mystr)
        search=pattern.findall(mytest)
        if search:
            return True
        else:
            return False

if __name__ == '__main__':
    unittest.main()