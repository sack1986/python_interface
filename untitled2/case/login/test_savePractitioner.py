# coding:utf-8

import unittest
import requests
from selenium import webdriver
import time
import re


class TestSavePractitioner(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_save_practitioner(self):

        url = "http://192.168.0.236:8180/fdczzxt/company/savePractitioner"

        payload = "fName=%E6%9D%8E%E5%9B%9B&fState=2&fCompany.id=11941&fOperateDate=2020-09-02&id=138177&fRecordType=RY&fChangeType=&fChangeID=&fLicenseType.id=102&fLicenseNo=108108&fBirthDay=&fEducation.id=2301&fTelephone=13222020202&fIsRightMan=0&fManagerType.id=4001&fChargeType.id=4002&fIsProfession=0&fNationality.id=2101&fType.id=2007&fJobTitle.id=2415&fProfession.id=2201&fContractBeginDate=2020-09-01&fContractEndDate=%E6%97%A0&fWorking=&prac=1"
        headers = {
            'Accept':'text/html,application/xhtml+xml, image/jxr,*/*',
            'Referer':'http://192.168.0.236:8180/fdczzxt/company/savePractitioner',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh - CN',
            'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64;Trident/7.0;rv: 11.0)likeGecko',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept-Encoding':'gzip, deflate',
            'Host':'192.168.0.236:8180',
            'Connection':'Keep-Alive',
            'Pragma':'no-cache',
            'Cookie':'JSESSIONID=4D00A498E438A0D2C92EE8A67EFE8A58'
       }

        response = requests.request("POST", url, headers=headers, data=payload)
        mytest1=response.text
        print(mytest1)
        mystr1="108108"
        result=TestSavePractitioner.my_verify(self,mytest1,mystr1)
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