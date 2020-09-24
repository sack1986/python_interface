
import unittest
import requests
import json



class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_add(self,url,headers,**data):
        url = "http://220.165.8.55:8891/capitalFlow/saveForDeposit"
        mydata=data
        id=mydata['id']
        superviseNo=mydata['superviseNo']
        projectNo=mydata['projectNo']
        sourceCertNo=mydata['sourceCertNo']
        sourceCertType=mydata['sourceCertType']
        contractCode=mydata['contractCode']
        transactionNo=mydata['transactionNo']
        amount=mydata['amount']
        sourcePayNameTemp=mydata['sourcePayNameTemp']
        sourceAccountName=mydata['sourceAccountName']
        sourceAccountNo=mydata['sourceAccountNo']
        sourceBankName=mydata['sourceBankName']
        sourceBankName=mydata['sourceBankName']
        sourceBankCode=mydata['sourceBankCode']
        payTime=mydata['payTime']
        remark=mydata['remark']
        operatorName=mydata['operatorName']
        operatorCertType=mydata['operatorCertType']
        operatorCertNo=mydata['operatorCertNo']
        sourcePayName=mydata['sourcePayName']

        payload ={
            'id':id,
            'superviseNo':superviseNo,
            'projectNo':projectNo,
            'sourceCertNo':sourceCertNo,
            'sourceCertType':sourceCertType,
            'contractCode':contractCode,
            'transactionNo':transactionNo,
            'amount':amount,
            'sourcePayNameTemp':sourcePayNameTemp,
            'sourceAccountName':sourceAccountName,
            'sourceAccountNo':sourceAccountNo,
            'sourceBankName':sourceBankName,
            'sourceBankCode':sourceBankCode,
            'payTime':payTime,
            'remark':remark,
            'operatorName':operatorName,
            'operatorCertType':operatorCertType,
            'operatorCertNo':operatorCertNo,
            'sourcePayName':sourcePayName
        }



        response = requests.request("POST", url, headers=headers, data=payload)
        text=response.json()
        #获取返回结果中message的内容
        message=text["message"]
        #获取返回结果中新增的记录id值
        if message=="保存成功":
            id=text["result"]["id"]
        else:
            id='NULL'
        return message,id



if __name__ == '__main__':
    unittest.main()