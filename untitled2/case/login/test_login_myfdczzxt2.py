
import unittest
import requests
from selenium import webdriver
import time
import re
from common.sqlserver import *


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.j_username=[]
        self.j_password=[]
        self.j_verify=[]

        ms = MSSQL.Ms(self)
        #ms = MSSQL(host="localhost", user="sa", pwd="xqx1234", db="test_fdczzxt")
        reslist = ms.Selsql("select * from info")
        for i in reslist:
            self.j_username.append(i[1])
            self.j_password.append(i[2])
            self.j_verify.append(i[3])
        print("test case start")


    def tearDown(self):
        print("test case end")

    def test_login(self):
        url = "http://192.168.0.236:8180/fdczzxt/j_spring_security_check"
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
        list_count=len(self.j_username)
        i=0
        while(i<list_count):
            payload = "j_username="+self.j_username[i]+"&j_password="+self.j_password[i]
            print(self.j_username[i],self.j_password[i])
            payload=payload.encode('utf-8')
            response = requests.request("POST", url, headers=headers, data=payload)
            mytest1=response.text
            mystr1=self.j_verify[i]
            result=TestLogin.my_verify(self,mytest1,mystr1)
            return self.assertEqual(result,True)
            i=i+1


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