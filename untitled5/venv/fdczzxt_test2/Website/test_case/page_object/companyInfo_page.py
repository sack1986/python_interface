from page_object.base_page import *
from selenium.webdriver.common.by import By


class CompanyInfoPage(Page):
    """首页登录页面"""
    url = '/login'
    # 定位器
    companyManageMenu_loc=(By.XPATH,'//a[contains(text(),'企业信息管理')]')
    companyInfoMenu_loc=(By.XPATH,'//a[contains(text(),'企业基本信息')]')
    fCompanyName_loc=(By.ID,'fCompanyName')
    fDepartment_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/button[1]')
    fProvince_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/button[1]/span[1]')
    fCity_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/div[2]/button[1]/span[1]')
    fCountry_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/div[3]/button[1]/span[1]')
    fStreet_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/button[1]/span[1]')
    fTown_loc=(By.ID,'fTown')
    fStreetAddress_loc=(By.ID,'fStreetAddress')
    fCommunity_loc=(By.ID,'fCommunity')
    fCompanyAddress_loc=(By.ID,'fCompanyAddress')
    fBusinessStatus_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/button[1]/span[1]')
    fBelong_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/button[1]/span[1]')
    fZiCompany_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[6]/td[1]/label[1]')
    #select
    fCompanyTypeOne_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[7]/td[1]/div[1]/button[1]/span[1]')
    fCompanyTypeTwo_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[7]/td[1]/div[2]/button[1]/span[1]')

    fCompanyHolding_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[8]/td[1]/div[1]/button[1]/span[1]')
    fCountryHolding_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[8]/td[2]/div[1]/button[1]/span[1]')
    fContactPeople_loc=(By.ID,'fContactPeople')
    fPhone_loc=(By.ID,'fPhone')
    fTelephone_loc=(By.ID,'fTelephone')
    fFax_loc=(By.ID,'fFax')
    fEmail_loc = (By.ID, 'fEmail')
    fPost_loc = (By.ID, 'fPost')
    fWebsite_loc = (By.ID, 'fWebsite')
    fIntroduction_loc = (By.ID, 'fIntroduction')
    fMemo_loc = (By.ID, 'fMemo')
    fCapital_loc = (By.ID, 'fCapital')
    #日期控件
    fCapital_loc = (By.ID, 'fCapital')
    #日期控件
    fBusinessBeginDate_loc = (By.ID, 'fBusinessBeginDate')
    fBusinessEndDate_loc = (By.ID, 'fBusinessEndDate')
    fBusinessNum_loc = (By.ID, 'fBusinessNum')fRegisterDepartment
    fRegisterDepartment_loc = (By.ID,'fRegisterDepartment')
    #上传图片

    fRegisterDepartment_loc = (By.ID, 'fRegisterDepartment')
    #日期控件
    fRegidterDate_loc = (By.ID, 'fRegidterDate')
    fBusinessMemoOne_loc = (By.ID, 'fBusinessMemoOne')
    fBusinessMemoTwo_loc = (By.ID, 'fBusinessMemoTwo')
    fBusinessMemoThree_loc = (By.ID, 'fBusinessMemoThree')
    #保存按钮
    saveCompanyButton_loc=(By.ID,'saveCompanyButton')



    username_loc = (By.ID, 'j_username')
    password_loc = (By.ID, 'j_password1')
    submit_loc = (By.ID, 'loginclick')

    # 用户名输入框元素
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 密码输入框元素
    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    # 登录功能模块封装
    def Login_action(self, username, password):
        """测试用户名密码是否可以登录"""
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    LoginPass_loc = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/span[1]')
    LoginFail_loc = (By.XPATH, '/html[1]/body[1]/div[5]/p[1]')

    # 登录成功的情况
    def type_loginPass_hint(self):
        return self.find_element(*self.LoginPass_loc).text

    # 登录失败的情况
    def type_loginFail_hint(self):
        return self.find_element(*self.LoginFail_loc).text


