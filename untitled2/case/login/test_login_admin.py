
import unittest
import requests


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_login(self):
        url = "http://oauth2.192-168-0-240.nip.io"

        payload = "username=admin&password=xqx1234&_sig=05XBa8EtGVqtX0rzvVYJMIN_JRPifVQ9U7XJiLx0dS0fbmMcwDeYitLYORZLqFcPRr1j8ti5kekxk16OztBrIEhS2DIQY-1h69AXjot45RwTU3HoAeVaBTVEiTLm7nfOLtf6AS1bVCxJ3tNeDm-3xv5aVWtgIIbwQW1PUaXJqB7MWGLZH5hst31_M6QMH0WE50pPKfE3Qk9P1sK2JuXqR8Cg8JSBh1A4X76EHFX6-i09yGEll6xknwp5wUKFdB3mHT4ZKOSsUohKcIkJm78AYiT9mSxyd90r1PDoe7EKQFq3-laQOXzTPszLtynSlqJkIXHo9P43DCQpRiPSmL_a744g&_token=1594372907864%3A0.4454426894484607&_session_id=01nulCTvYYUR-fHKl5JV_hMlCoPHXfGifsIRKmIcvIM_2IvTBC6qEYk5VhzNyBNzFN0_kOuI7aoET_gJMqiPtuOdjVi-FhcxfFRyzZpmuoC5BypbdxU97CpNssyX9kcqkv&_scene=ic_login"
        headers = {
            'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
            'Referer':'http://oauth2.192-168-0-240.nip.io/login',
            'Accept-Language':'zh-CN',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept-Encoding':'gzip, deflate',
            'Content-Length':'582',
            'Host':'oauth2.192-168-0-240.nip.io',
            'Connection':'Keep-Alive',
            'Pragma':'no-cache',
            'Cookie':'SESSION=ZGM3OWU1MTItZWU1Zi00NTk2LWE5NWYtMDk4YTAyODAxODg1'

        }

        response = requests.request("POST", url, headers=headers, data=payload)
        #response = requests.request("POST", url, headers=headers)

        print(response.text.encode('utf8'))

if __name__ == '__main__':
    unittest.main()