from selenium import webdriver
from model import myunitest
from model.function_zd import Screen
from page_object.login_page import *
from time import sleep
import unittest
from driver.driver import *
from page_object.base_page import *
import time
"""
@测试用例设计
用户名密码正确登录
用户名正确密码错误登录
用户名和密码为空登录
"""
class LoginTest(unittest.TestCase):

    mydriver=browser()
    page=f(mydriver)



    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename1='fdczzxt_login1_normal_'+nowtime+'.png'
    @Screen(mydriver,filename1)
    #@Screen(mydriver)
    def test_login1_normal(self):
        """用户名密码正确登录"""
        self.page.open()
        po=LoginPage(self.mydriver)
        po.Login_action('昆明万睿房地产开发有限公司','1234')
        sleep(3)
        #断言与截图

        self.assertEqual(po.type_loginPass_hint(), '退出系统')


        print('test_login1_normal is test end')

    filename2 = 'fdczzxt_login2_passwdErro_' + nowtime + '.png'
    @Screen(mydriver, filename2)
    def test_login2_passwdError(self):
        """用户名正确密码错误登录"""
        self.page.open()
        po=LoginPage(self.mydriver)
        po.Login_action('administrator27878','1234')
        sleep(3)
        #断言与截图
        self.assertEqual(po.type_loginFail_hint(), '用户名无效')

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

