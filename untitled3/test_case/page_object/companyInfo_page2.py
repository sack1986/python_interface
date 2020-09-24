from page_object.base_page import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class CompanyInfoPage(Page):

    # 定位器
    companyManageMenu_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[2]/a[1]')
    companyInfoMenu_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]')

    #fCity_loc = (By.XPATH, '/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/div[2]/button[1]')
    fDepartment_loc = (By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/button[1]')
    fDepartment_loc4=(By.ID,'fDepartment')
    # fDepartment_loc2 = (By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/div[2]/div[1]/ul')
    # fDepartment_loc3 = (By.XPATH,'li')
    fSubCompany_loc=(By.XPATH,"//*/input[@type='radio']")  #子公司
    fSelectCompanyButton_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[6]/td[2]/button[1]') #选择总公司按钮


    fSelectCompanyName_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/form[1]/input[1]')  #公司名称查询条件输入框
    fSearchButton_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/form[1]/input[4]') #查询按钮
    fSelectCompany_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/button[1]')  #选择公司
    fBusinessMemoOne_loc = (By.ID, 'fBusinessMemoOne')
    fBusinessMemoTwo_loc = (By.ID, 'fBusinessMemoTwo')
    fBusinessMemoThree_loc = (By.ID, 'fBusinessMemoThree')
    #保存按钮
    saveCompanyButton_loc=(By.ID,'saveCompanyButton')


    def type_companyManageMenu(self):
        self.find_element(*self.companyManageMenu_loc).click()

    def type_companyInfoMenu(self):
        self.find_element(*self.companyInfoMenu_loc).click()

     # 主管部门
    def type_fDepartment(self,driver):


        myfDepartmentself=self.find_element(*self.fDepartment_loc)
        myfDepartmentself.send_keys(Keys.ENTER)
        selectDepartment=ActionChains(driver)
        selectDepartment.send_keys(Keys.ARROW_DOWN)
        selectDepartment.send_keys(Keys.ARROW_DOWN)
        selectDepartment.send_keys(Keys.ENTER)
        selectDepartment.perform()





        #myfDepartmentself2 = myfDepartmentself.find_elements(*self.fDepartment_loc3)
        #print("值：", myfDepartmentself2[2].text)


    #子公司
    def type_fSubCompany(self):
        fSubCompanys=self.find_elements(*self.fSubCompany_loc)
        if fSubCompanys:
            fSubCompanys[1].click()


    #选择总公司按钮
    def type_fSelectCompanyButton(self,driver):
        fSelectCompanyButton_loc2=self.find_element(*self.fSelectCompanyButton_loc)
        action=ActionChains(driver)
        action.move_to_element(fSelectCompanyButton_loc2)# 移动到元素上
        action.click()
        action.perform()



        # 公司搜索条件
    def type_fSelectCompanyName(self,driver):
        # ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        # time.sleep(2)
                self.find_element(*self.fSelectCompanyName_loc).send_keys("测试")


        # 搜索按钮
    def type_fSearchButton(self):
        self.find_element(*self.fSearchButton_loc).click()

    # 选择总公司
    def type_fSelectCompany(self,driver):
        fSelectCompany_loc2 = self.find_element(*self.fSelectCompany_loc)
        action = ActionChains(driver)
        action.move_to_element(fSelectCompany_loc2)  # 移动到元素上
        action.click()
        action.perform()

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

    # 保存按钮元素
    def type_submit(self):
        self.find_element(*self.saveCompanyButton_loc).click()

    # 保存功能模块封装
    def saveCompany_action(self,driver, fBusinessMemoOne,fBusinessMemoTwo,fBusinessMemoThree):
        """保存"""
        nowhandle=driver.current_window_handle
        self.type_companyManageMenu()
        self.type_companyInfoMenu()
        self.type_fSubCompany()
        time.sleep(5)
        self.type_fDepartment(driver)
        #选择总公司
        self.type_fSelectCompanyButton(driver)
        time.sleep(5)
        driver.switch_to_frame('dynamicModalCompanyFrame')
        self.type_fSelectCompanyName(driver)
        self.type_fSearchButton()
        self.type_fSelectCompany(driver)
        # 基本信息页面
        driver.switch_to_window(nowhandle)
        #经营范围
        self.type_fBusinessMemoOne(fBusinessMemoOne)
        self.type_fBusinessMemoTwo(fBusinessMemoTwo)
        self.type_fBusinessMemoThree(fBusinessMemoThree)
        self.type_submit()

    message_loc=(By.XPATH,'/html[1]/body[1]/div[9]/h2[1]')
    # 保存成功的情况
    def type_savePass_hint(self):
        return self.find_element(*self.message_loc).text



