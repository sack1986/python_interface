from selenium import webdriver
from test_case.model import myunitest
from test_case.model.function_zd import Screen
from test_case.page_object.login_page import *
from test_case.page_object.practitionerInfo_page import *
from time import sleep
import unittest
from driver.driver import *
from test_case.page_object.base_page import *
import time
"""
@测试用例设计
修改人员信息
"""
class PractitionerTest(unittest.TestCase):
    #@unittest.skip('skip this case)
    mydriver = browser()
    page = Page(mydriver)
    page.open()

    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename_login = 'fdczzxt_login_normal_' + nowtime + '.png'
    filename_saveCompany = 'fdczzxt_company_save_' + nowtime + '.png'

    #
    @Screen(mydriver, filename_login)
    # # @Screen(mydriver)
    def test_modify_pactitioner(self):
        """用户名密码正确登录"""
        print("test_login1_normal start run...")
        po = LoginPage(self.mydriver)
        po.Login_action('测试机构', 'a1234567')
        sleep(5)
        # 断言与截图
        self.assertEqual(po.type_loginPass_hint(), '退出系统')


        #修改个人信息
        practitioner=practitionerInfoPage(self.mydriver)
        practitioner.modifyPractitioner_action(self.mydriver,"杭梅梅","530127198520202020","13888202020")



