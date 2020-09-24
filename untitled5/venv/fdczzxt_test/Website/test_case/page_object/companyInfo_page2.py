from page_object.base_page import *
from selenium.webdriver.common.by import By
import time


class CompanyInfoPage(Page):

    # 定位器
    companyManageMenu_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[2]/a[1]')
    companyInfoMenu_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]')

    fBusinessMemoOne_loc = (By.ID, 'fBusinessMemoOne')
    fBusinessMemoTwo_loc = (By.ID, 'fBusinessMemoTwo')
    fBusinessMemoThree_loc = (By.ID, 'fBusinessMemoThree')
    #保存按钮
    saveCompanyButton_loc=(By.ID,'saveCompanyButton')

    # 经营范围一
    def type_companyManageMenu(self):
        self.find_element(*self.companyManageMenu_loc).click()

    def type_companyInfoMenu(self):
        self.find_element(*self.companyInfoMenu_loc).click()

    # 经营范围一
    def type_fBusinessMemoOne(self, fBusinessMemoOne):
        self.find_element(*self.fBusinessMemoOne_loc).clear()
        self.find_element(*self.fBusinessMemoOne_loc).send_keys(fBusinessMemoOne)

    # 经营范围二
    def type_fBusinessMemoTwo(self, fBusinessMemoTwo):
        self.find_element(*self.fBusinessMemoTwo_loc).clear()
        self.find_element(*self.fBusinessMemoTwo_loc).send_keys(fBusinessMemoTwo)

    # 经营范围三
    def type_fBusinessMemoThree(self, fBusinessMemoThree):
        self.find_element(*self.fBusinessMemoThree_loc).clear()
        self.find_element(*self.fBusinessMemoThree_loc).send_keys(fBusinessMemoThree)

    # 登录按钮元素
    def type_submit(self):
        self.find_element(*self.saveCompanyButton_loc).click()

    # 登录功能模块封装
    def saveCompany_action(self, fBusinessMemoOne,fBusinessMemoTwo,fBusinessMemoThree):
        """测试用户名密码是否可以登录"""
        self.type_companyManageMenu()
        self.type_companyInfoMenu()
        self.type_fBusinessMemoOne(fBusinessMemoOne)
        self.type_fBusinessMemoTwo(fBusinessMemoTwo)
        self.type_fBusinessMemoThree(fBusinessMemoThree)
        self.type_submit()

    message_loc=(By.XPATH,'/html[1]/body[1]/div[9]/h2[1]')
    # 保存成功的情况
    def type_savePass_hint(self):
        return self.find_element(*self.message_loc).text



