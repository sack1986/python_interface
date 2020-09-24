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
新增人员信息
"""
class PractitionerTest(unittest.TestCase):
    #@unittest.skip('skip this case)
    mydriver = browser()
    page = Page(mydriver)
    page.open()

    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename_add = 'fdczzxt_practitioner_add_' + nowtime + '.png'

    #
    @Screen(mydriver, filename_add)
    # # @Screen(mydriver)
    def test_add_pactitioner(self):
        """用户名密码正确登录"""
        print("test_login1_normal start run...")
        po = LoginPage(self.mydriver)
        po.Login_action('测试机构3', 'a1234567')
        sleep(5)
        # 断言与截图
        self.assertEqual(po.type_loginPass_hint(), '退出系统')


        #新增人员
        data={
            "fName":"人员22002",
            "fLicenseType":"护照",
            "fLicenseNo":"22002",
            "fBirthDay":"2020-10-01",
            "fEducation":"2301",
            "fTelephone": "13222020202",
            "fIsRightMan": "是",
            "fManagerType": "不是",
            "fChargeType": "不是",
            "fIsProfession": "是",
            "fGender": "女",
            "fNationality": "中华人民共和国",
            "fType": "会计",
            "fJobTitle": "2402",
            "fProfession": "结构",
            "fContractBeginDate": "2020-10-02",
            "fContractEndDate": "无"

        }
        # 新增个人信息
        practitioner = practitionerInfoPage(self.mydriver)
        practitioner.addPractitioner_action(self.mydriver, **data)
        # 断言与截图
        self.assertEqual(practitioner.type_savePass_hint(), '保存成功')




