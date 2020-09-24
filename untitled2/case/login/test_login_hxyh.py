
import unittest
import requests


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_login(self):
        url = "http://oauth2.192-168-0-240.nip.io"

        payload = "username=hxyh01&password=xqx1234&_sig=05XBa8EtGVqtX0rzvVYJMIN0cmA5G99ykxHog_GoCh7KZ5tMC5Gol6tsFfTZDuG2_NOUXvt-vZCOaIZDiPhhpAuUdP-OgTjmmmWY5ALdTSZE-hyUzfUJzZN2Yi03ApQSrO0BfVGpgKhp25RpS-aaTrNlKxZfrMpbtmHZLoxXQlytUrYNt3igZVweSSFnGtvZbk9s3OV5rnrErPq41ww2VPNPpzgiVUnH_hNETF72jqYr7V5lftRZoUk8iyn6BV3rWFRL4ziMOjpRZ6ANqDDQ6-O2FXj59VAy3SxLhS5b0V3WaLGpaLsycS1jjOpHwtszC3YzWXcC61kmrMhfkjslXVGw&_token=1594605323235%3A0.06574011391978929&_session_id=01YJnK8kaUbvyZo_TxSdpAMb2rhOoPWC8vvGcosWnJjpAdDO_hZZ1JO42ijI7VSbWdsCU65hRRm-mXDWbrLpi98YJUOiSyXW0bf7Zh4I1Ni6KEYVPyGEc7Jgi5ruGlWqkN&_scene=ic_login"
        headers = {
            'Referer':'http://oauth2.192-168-0-240.nip.io/login',
            'Cache-Control':'max-age=0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN',
            'Content-Type':'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
            'Accept-Encoding':'gzip, deflate',
            'Content-Length':'584',
            'Host':'oauth2.192-168-0-240.nip.io',
            'Connection':'Keep-Alive',
            'Cookie':'SESSION=ZmUyZTMzOGItZDU0OS00NDgwLWE2YjAtYTMzOTk0M2Y5ZDc2'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

if __name__ == '__main__':
    unittest.main()