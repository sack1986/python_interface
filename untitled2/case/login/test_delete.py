
import unittest
import requests
import json


class TestDelete(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_delete(self,url,headers,**data):

        id=data['id']
        delReason=data['delReason']
        data={
            'id':id,
            'delReason':delReason
        }
        response = requests.request("POST", url, headers=headers, data=data)
        text=response.json()
        #result
        result=text["result"]

        return result



if __name__ == '__main__':
    unittest.main()