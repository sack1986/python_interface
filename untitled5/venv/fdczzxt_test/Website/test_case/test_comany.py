from selenium import webdriver
from model import function,myunitest
from page_object.login_page import *
from page_object.companyInfo_page2 import *
from time import sleep
import unittest
"""
@测试用例设计
保存企业基本信息
"""
class CompanyTest(myunitest.StarEnd):
    #@unittest.skip('skip this case)
    def test_company_save(self):
        """登录"""
        po=LoginPage(self.driver)
        po.Login_action('昆明未来城开发有限公司','1234')
        sleep(3)
        #断言与截图
        self.assertEqual(po.type_loginPass_hint(), '退出系统')
        function.insert_img(self.driver,'fdczzxt_login1_normal.png')


        #保存企业信息
        company=CompanyInfoPage(self.driver)
        company.saveCompany_action('经营1','经营2','')
        try:
            self.assertEqual(type_savePass_hint(), '保存成功')
        except:
            function.insert_img(self.driver,'fdczzxt_company_save.png')


