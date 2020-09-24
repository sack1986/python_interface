from selenium import webdriver
from model import myunitest
from model.function_zd import Screen
from page_object.login_page import *
from page_object.companyInfo_page2 import *
from time import sleep
import unittest
from driver.driver import *
from page_object.base_page import *
import time
"""
@测试用例设计
保存企业基本信息
"""
class CompanyTest(unittest.TestCase):
    #@unittest.skip('skip this case)

    mydriver = browser()
    page = Page(mydriver)
    page.open()

    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename_login = 'fdczzxt_login1_normal_' + nowtime + '.png'
    filename_saveCompany = 'fdczzxt_company_save_' + nowtime + '.png'
    #
    @Screen(mydriver, filename_login)
    # # @Screen(mydriver)
    def test_save_company(self):
        """用户名密码正确登录"""
        print("test_login1_normal start run...")
        po = LoginPage(self.mydriver)
        po.Login_action('测试企业', '1234')
        sleep(3)
        # 断言与截图
        self.assertEqual(po.type_loginPass_hint(), '退出系统')

    #保存企业信息
        company=CompanyInfoPage(self.mydriver)
        company.saveCompany_action(self.mydriver,'经营1','经营2','3')
        sleep(8)
        #断言与截图
        self.assertEqual(company.type_savePass_hint(), '保存成功')

        self.mydriver.quit()

    # @Screen(mydriver, filename_saveCompany)
    # def test_company_save(self):
    #
    #     #保存企业信息
    #     company=CompanyInfoPage(self.mydriver)
    #     company.saveCompany_action('经营1','经营2','')
    #     sleep(3)
    #     #断言与截图
    #     self.assertEqual(type_savePass_hint(), '保存成功')



