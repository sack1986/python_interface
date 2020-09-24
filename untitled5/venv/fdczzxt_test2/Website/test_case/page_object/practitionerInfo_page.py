from page_object.base_page import *
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class practitionerInfoPage(Page):

    # 定位器
    companyManageMenu_loc = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[2]/a[1]')
    practitionerInfoMenu_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]')

    #选择，修改
    select_loc=(By.XPATH,"//*/input[@type='radio']")
    modify_loc=(By.ID,'editPr')

    #新增
    add_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/button[6]')
    #填写基本信息
    name_loc = (By.ID, 'fName')
    licenseNo_loc = (By.ID, 'fLicenseNo')


    #保存基本信息
    save_simpleInfo=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/button[1]')

    #电话
    telephon_loc = (By.ID, 'fTelephone')

    #上传
    upload_loc=(By.ID,"upload")
    selectfile_loc = (By.ID,'rt_rt_1dl6o97t8jtj1uhl1apf8ekidh6')
    uploadfile_loc= (By.XPATH,"//div[@class='uploadBtn state-pedding']")

    #保存按钮
    savePractitionerButton_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[11]/td[1]/div[1]/button[1]')

    # 菜单
    def type_companyManageMenu(self):
        self.find_element(*self.companyManageMenu_loc).click()



    def type_practitionerInfoMenu(self):
        self.find_element(*self.practitionerInfoMenu_loc).click()


    # 选择
    def type_select(self,driver):
        radios=self.find_elements(*self.select_loc)
        if radios:  # 判断是否有找到元素
            for radio in radios:  # 循环点击找到的元素
                if(not radio.is_selected()):
                    time.sleep(5)
                    # ActionChains(driver).move_to_element(radio).perform()  # 移动到元素上
                    # ActionChains(driver).click(radio).perform()

                    radio.send_keys(Keys.ARROW_DOWN) #点击键盘向下箭头

                    #radio.send_keys(Keys.ARROW_UP)
                    #radio.send_keys(Keys.ENTER)
                    #radio.click()



                    time.sleep(2)
                    break




        # trs = self.findElement(By.xpath("/html/body/div[2]/div/div[2]/div[2]/div[2]/table")).findElements(By.tagName("tr"))   # 获取每一页所有的tr对象
        # WebElement
        # wbtr = Demo.getpoduct(trs, dr, By.className("datagrid-cell"))      # 获取具体的webElemnet对象（tr对象）
        # if (wbtr != null):
        #     s=wbtr.is_sele
        #     if (!wbtr.is_selected()):
        #         wbtr.click()     #返回对应的对象则点击选中
        #     else:
        #         System.out.println("选中产品时出错")



    # 修改

    def type_modify(self, ):
        self.find_element(*self.modify_loc).click()

    #新增
    def type_add(self ):
        self.find_element(*self.add_loc).click()
    # 姓名
    def type_name(self, name):
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.name_loc).send_keys(name)

   # 证件号

    def type_licenseNo(self, licenseNo):
        self.find_element(*self.licenseNo_loc).clear()
        self.find_element(*self.licenseNo_loc).send_keys(licenseNo)


    #保存基本信息
    def type_saveSimpleInfo(self ):
        self.find_element(*self.save_simpleInfo).click()

#电话
    def type_telephone(self, telephone):
        self.find_element(*self.telephon_loc).clear()
        self.find_element(*self.telephon_loc).send_keys(telephone)
    # 上传
    def type_upload(self ):
        self.find_element(*self.upload_loc).click()



    #选择上传文件
    def type_selectFile(self ):
        self.find_element(*self.selectfile_loc).click()

    # 上传文件
    def type_uploadFile(self):
        self.find_element(*self.uploadfile_loc).click()

    # 保存按钮元素
    def type_submit(self):
        self.find_element(*self.savePractitionerButton_loc).click()

    # 保存模块封装
    def savePractitioner_action(self,driver,name,licenseNo,telephone):
        """测试用户名密码是否可以登录"""
        self.type_companyManageMenu()
        time.sleep(4)
        self.type_practitionerInfoMenu()
        time.sleep(4)
        #修改
        self.type_select(driver)
        self.type_modify()
        self.type_submit()


        #新增
        # self.type_add()
        # time.sleep(4)
        # self.type_name(name)
        # self.type_licenseNo(licenseNo)
        # self.type_saveSimpleInfo()
        # time.sleep(4)
        # self.type_telephone(telephone)
        # time.sleep(6)
        # self.type_upload()
        # time.sleep(10)
        # # 打印所有的handle
        # all_handles = driver.window_handles
        # print(all_handles)
        #driver.switch_to.default_content()



        #self.type_selectFile()
        # ActionChains(driver).move_to_element(myselectFile).perform()  #移动到元素上
        # ActionChains(driver).click(myselectFile).perform()  # 鼠标单击按钮

        # os.system("upload/upload.exe")
        # self.type_uploadFile()
        #
        # self.type_submit()

    message_loc=(By.XPATH,'/html[1]/body[1]/div[7]/h2[1]')
    # 保存成功的情况
    def type_savePass_hint(self):
        return self.find_element(*self.message_loc).text



