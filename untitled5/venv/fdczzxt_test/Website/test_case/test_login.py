from selenium import webdriver
from model import function_zd,myunitest
from page_object.login_page import *
from time import sleep
import unittest
"""
@测试用例设计
用户名密码正确登录
用户名正确密码错误登录
用户名和密码为空登录
"""
class LoginTest(myunitest.StarEnd):
    #@unittest.skip('skip this case)
    def test_login1_normal(self):
        """用户名密码正确登录"""
        print("test_login1_normal start run...")
        po=LoginPage(self.driver)
        po.Login_action('昆明万睿房地产开发有限公司','12345')
        sleep(3)
        #断言与截图

        self.assertEqual(po.type_loginPass_hint(), '退出系统')
        function_zd.insert_img(self.driver,'fdczzxt_login1_normal.png')

        print('test_login1_normal is test end')
    def test_login2_passwdError(self):
        """用户名正确密码错误登录"""
        print("test_login2_passwdError start run...")
        po=LoginPage(self.driver)
        po.Login_action('administrator2','1234')
        sleep(3)
        #断言与截图
        self.assertEqual(po.type_loginFail_hint(), '用户名无效')
        function.insert_img(self.driver,'fdczzxt_login2_passwdError.png')
        print('test_login2_passwdError is test end')
    # def test_login3_empty(self):
    #     """用户名和密码为空登录"""
    #     print("test_login3_empty start run...")
    #     po=LoginPage(self.driver)
    #     po.Login_action('','')
    #     sleep(3)
    #     #断言与截图
    #     self.assertEqual(po.type_loginFail_hint(), '必填项')
    #     function.insert_img(self.driver,'login3_empty.png')
    #     print('test_login3_empty is test end')

