
import unittest
import requests
import json
#from case.login import test_add
from case.login  import test_delete
import time

class TestApi(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_api_delete(self):
        url = "http://220.165.8.55:8891/capitalFlow/deleteCapitalFlowById"
        headers = {
            'POST http': '//220.165.8.55:8891/capitalFlow/deleteCapitalFlowById HTTP/1.1',
            'Origin': 'http://220.165.8.55:8891',
            'Referer': 'http://220.165.8.55:8891/capitalFlow/capitalJump',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
            'Content-Length': '52',
            'Host': '220.165.8.55:8891',
            'Connection': 'Keep-Alive',
            'Pragma': 'no-cache',
            'Cookie': 'JSESSIONID=547CDED9C4BA4047CE07D9D12514D895; Hm_lvt_71f7be1481d31847831b556ee2d18492=1587018963'
        }
        mydata = {
            'id': '52',
            'delReason': '测试删除'
        }
        result = test_delete.TestDelete.test_delete(self, url, headers, **mydata)
        message = result
        return self.assertEqual(message, "删除成功")
'''
    def test_api_add(self):
        url = "http://220.165.8.55:8891/capitalFlow/saveForDeposit"

        headers = {
            'Origin':'http://220.165.8.55:8891',
            'Referer':'http://220.165.8.55:8891/capitalFlow/forwardTo/add/JGKM20200706001/-1',
            'Accept':'*/*',
            'Accept-Language':'zh-CN',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With':'XMLHttpRequest',
            'Accept-Encoding':'gzip, deflate',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
            'Content-Length':'833',
            'Host':'220.165.8.55:8891',
            'Connection':'Keep-Alive',
            'Pragma':'no-cache',
            'Cookie':'Hm_lvt_71f7be1481d31847831b556ee2d18492=1587018963;JSESSIONID=547CDED9C4BA4047CE07D9D12514D895'
        }

        now = time.strftime("%Y-%m-%d %H:%M:%S")
        mydata ={
            'id':'',
            'superviseNo':'JGKM20200706001',
            'projectNo':'KMQFBA-20200416004',
            'sourceCertNo':'530127198606092727',
            'sourceCertType':'居民身份证',
            'contractCode':'NKM0057560001',
            'transactionNo':'5516',
            'amount':'10000.00',
            'sourcePayNameTemp':'代绍丽,居民身份证,530127198606092727',
            'sourceAccountName':'李四',
            'sourceAccountNo':'6321120200003001',
            'sourceBankName':'交通银行',
            'sourceBankCode':'6321120200003002',
            'payTime':now,
            'remark':'没有备注',
            'operatorName':'华夏银行股份有限公司昆明分行',
            'operatorCertType':'营业执照',
            'operatorCertNo':'91530000916558696A',
            'sourcePayName':'代绍丽'
        }
        result = test_add.TestAdd.test_add(self, url, headers, **mydata)
        message=result[0]
        self.id=result[1]
        return self.assertEqual(message,"保存成功")
'''






if __name__ == '__main__':
    unittest.main()