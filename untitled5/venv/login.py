import requests
import unittest


cookies = {
    'JSESSIONID': 'EB92403E344EE057B8EF84D2602E39C2',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://192.168.0.249:9080',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://192.168.0.249:9080/fdczzxt/login;jsessionid=EB92403E344EE057B8EF84D2602E39C2',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

data = {
  'j_username': 'dhzrlszjjcl^',
  'j_password': '1234'
}




response = requests.post('http://192.168.0.249:9080/fdczzxt/j_spring_security_check', headers=headers,
                             cookies=cookies, data=data, verify=False)



