from page_object.base_page import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    """首页登录页面"""
    url = '/login'
    # 定位器
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


