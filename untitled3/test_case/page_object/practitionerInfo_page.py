from test_case.page_object.base_page import *
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import subprocess
from pywinauto import Desktop


class practitionerInfoPage(Page):

    # 定位器
    companyManageMenu_loc = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[2]/a[1]')
    practitionerInfoMenu_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]')

    #选择，修改
    select_loc=(By.XPATH,"//*/input[@type='radio']")
    modify_loc=(By.ID,'editPr')

    #新增
    add_loc=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/button[6]')

    #保存基本信息
    save_simpleInfo=(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/button[1]')

    """
    新增人员信息
    """
    fName_loc=(By.ID, 'fName')
    fLicenseType_loc=(By.ID, 'fLicenseType')
    fLicenseNo_loc = (By.ID, 'fLicenseNo')
    fBirthDay1_loc=(By.ID, 'fBirthDay')
    BirthDay='fBirthDay'
    fBirthDay_loc= (By.XPATH, "//tr[3]//td[2]//div[1]//span[1]//button[1]")
    fBirthDayDate_loc = (By.XPATH, " / html[1] / body[1] / div[5] / div[1] / table[1] / tbody[1] / tr[3] / td[3]")
    fEducation_loc= (By.ID, 'fEducation')
    fTelephone_loc= (By.ID, 'fTelephone')
    fIsRightMan_loc= (By.ID, 'fIsRightMan1')
    fManagerType_loc= (By.ID, 'fManagerType')
    fChargeType_loc= (By.ID, 'fChargeType')
    fIsProfession_loc= (By.XPATH, '//tr[5]//td[2]//input[2]')
    fGender_loc = (By.ID, 'fGender2')
    fNationality_loc = (By.ID, 'fNationality')
    fType_loc = (By.ID, 'fType')
    fJobTitle_loc = (By.ID, 'fJobTitle')
    fProfession_loc = (By.ID, 'fProfession')
    fContractBeginDate_loc = (By.ID, 'fContractBeginDate')
    ContractBeginDate='fContractBeginDate'
    fContractEndDate_loc = (By.ID, 'fContractEndDate')
    dynamicModalFrame_loc="dynamicModalFrame"
    notice_loc= (By.XPATH, "//button[@class='confirm btn btn-lg btn-primary']")
    close_loc = (By.XPATH, "//button[contains(text(),'×')]")
    #电话
    telephon_loc = (By.ID, 'fTelephone')

    #上传护照
    upload_loc=(By.ID,"upload") #上传护照
    selectfile_loc = (By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]')
    uploadfile_loc= (By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]')

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

    """
    新增人员信息
    """

    # 姓名
    def type_fName(self, fName):
        self.find_element(*self.fName_loc).clear()
        self.find_element(*self.fName_loc).send_keys(fName)

    # 证件类型
    def type_fLicenseType(self, fLicenseType):
        s=self.find_element(*self.fLicenseType_loc)
        self.select_element(s,fLicenseType)
    # 证件号码
    def type_fLicenseNo(self, fLicenseNo):
        self.find_element(*self.fLicenseNo_loc).clear()
        self.find_element(*self.fLicenseNo_loc).send_keys(fLicenseNo)

     # 生日方法一：
    def type_fBirthDay1(self,fBirthDay1):
        self.find_element(*self.fBirthDay1_loc).send_keys(fBirthDay1)

    #生日方法二（1）
    def type_fBirthDay(self):
       return self.find_element(*self.fBirthDay_loc)

     # 生日日期方法二（2）
    def type_fBirthDayDate(self):
        return self.find_element(*self.fBirthDayDate_loc)
        # 证学历情况

    def type_fEducation(self, fEducation):
        s = self.find_element(*self.fEducation_loc)
        self.select_element(s, fEducation)
    # 电话
    def type_fTelephone(self, fTelephone):
        self.find_element(*self.fTelephone_loc).clear()
        self.find_element(*self.fTelephone_loc).send_keys(fTelephone)

        # 是否法人

    def type_fIsRightMan(self):
        self.find_element(*self.fIsRightMan_loc).click()
    # 是否总副经理
    def type_fManagerType(self, fManagerType):
        s=self.find_element(*self.fManagerType_loc)
        self.select_element(s,fManagerType)
    # 是否业务负责人
    def type_fChargeType(self, fChargeType):
        s=self.find_element(*self.fChargeType_loc)
        self.select_element(s,fChargeType)
    # 是否专业人员
    def type_fIsProfession(self):
        self.find_element(*self.fIsProfession_loc).click()
    #性别
    def type_fGender(self,):
        self.find_element(*self.fGender_loc).click()
    # 国籍
    def type_fNationality(self, fNationality):
        s=self.find_element(*self.fNationality_loc)
        self.select_element(s,fNationality)
        # 职务

    def type_fType(self, fType):
        s = self.find_element(*self.fType_loc)
        self.select_element(s, fType)
        # 职称
    def type_fJobTitle(self, fJobTitle):
        s = self.find_element(*self.fJobTitle_loc)
        self.select_element(s, fJobTitle)
        # 职称专业
    def type_fProfession(self, fProfession):
        s = self.find_element(*self.fProfession_loc)
        self.select_element(s, fProfession)
    # 合同开始日期
    def type_fContractBeginDate(self, fContractBeginDate):
        self.find_element(*self.fContractBeginDate_loc).send_keys(fContractBeginDate)
    # 合同结束日期
    def type_fContractEndDate(self, fContractEndDate):
        self.find_element(*self.fContractEndDate_loc).send_keys(fContractEndDate)
    # 切换iframe
    def type_switch_iframe(self):
        self.switch_iframe(self.dynamicModalFrame_loc)
    # 释放iframe
    def type_default_iframe(self):
        self.default_iframe()
    # 关闭上传成功提示信息
    def type_notice(self):
        self.find_element(*self.notice_loc).click()
    # 关闭上传窗口
    def type_close(self):
        self.find_element(*self.close_loc).click()

#电话
    def type_telephone(self, telephone):
        self.find_element(*self.telephon_loc).clear()
        self.find_element(*self.telephon_loc).send_keys(telephone)
    # 上传护照
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

    # 修改保存模块封装
    def modifyPractitioner_action(self,driver,name,licenseNo,telephone):
        """点击菜单进入操作页面"""
        self.type_companyManageMenu()
        time.sleep(4)
        self.type_practitionerInfoMenu()
        time.sleep(4)
        #修改
        self.type_select(driver)
        self.type_modify()
        self.type_submit()

    # 新增保存模块封装
    def addPractitioner_action(self,driver, **para):
        """点击菜单进入操作页面"""
        self.type_companyManageMenu()
        time.sleep(4)
        self.type_practitionerInfoMenu()
        time.sleep(4)
        #新增
        self.type_add()
        time.sleep(4)
        self.type_fName(para["fName"])
        self.type_fLicenseType(para["fLicenseType"])
        self.type_fLicenseNo(para["fLicenseNo"])
        self.type_saveSimpleInfo()
        time.sleep(4)

        # self.type_fName(para["fName"])
        # self.type_fLicenseType(para["fLicenseType"])
        # self.type_fLicenseNo(para["fLicenseNo"])
        #生日方法1
        # 介绍4中操作方法
        js = "document.getElementById('"+self.BirthDay+"').removeAttribute('readonly')"  # 1.原生js，移除属性
        # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
        # js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
        #js = "$('input[id=fBirthDay]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        driver.execute_script(js)
        self.type_fBirthDay1(para["fBirthDay"])
        #生日方法2
        # myfBirthDay=self.type_fBirthDay()
        # ActionChains(driver).move_to_element(myfBirthDay).perform()  #移动到元素上
        # ActionChains(driver).click(myfBirthDay).perform()  # 鼠标单击按钮
        # myfBirthDayDate = self.type_fBirthDayDate()
        # ActionChains(driver).move_to_element(myfBirthDayDate).perform()  # 移动到元素上
        # ActionChains(driver).click(myfBirthDayDate).perform()  # 鼠标单击按钮

        #self.type_fEducation(para["fEducation"])
        self.type_fTelephone(para["fTelephone"])
        self.type_fIsRightMan()
        self.type_fManagerType(para["fManagerType"])
        self.type_fChargeType(para["fChargeType"])
        self.type_fGender()
        self.type_fNationality(para["fNationality"])
        self.type_fType(para["fType"])
        self.type_fJobTitle(para["fJobTitle"])
        self.type_fIsProfession()
        time.sleep(4)
        self.type_fProfession(para["fProfession"])
        self.type_fContractBeginDate(para["fContractBeginDate"])

        js = "document.getElementById('" + self.ContractBeginDate + "').removeAttribute('readonly')"  # 1.原生js，移除属性
        # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
        # js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
        # js = "$('input[id=fBirthDay]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        driver.execute_script(js)
        self.type_fContractBeginDate(para["fContractBeginDate"])

        self.type_fContractEndDate(para["fContractEndDate"])

        time.sleep(6)
        self.type_upload()
        time.sleep(10)

        # # 切换到上传ifame：dynamicModalFrame
        # all_handles = driver.window_handles
        # print(all_handles)
        # driver.switch_to.default_content()
        self.type_switch_iframe()
        #
        #
        self.type_selectFile()
        # ActionChains(driver).move_to_element(myselectFile).perform()  #移动到元素上
        # ActionChains(driver).click(myselectFile).perform()  # 鼠标单击按钮
        #self.type_default_iframe()
        #打开上传的文件
        # filepath="C:\\Users\\test\\PycharmProjects\\untitled3\\test_case\\page_object\\upload\\upload.exe"
        # os.system(filepath)
        #subprocess.call(filepath)
        # 操作系统的指令，打开上传的文件
        wd = Desktop()
        open = wd['打开']  # 根据名字找到弹出窗口
        open["Edit1"].type_keys("C:\\Users\\test\\PycharmProjects\\untitled3\\test_case\\page_object\\upload\\test.pdf")  # 在输入框中输入值
        open["Button1"].click()
        time.sleep(10)



        #self.type_selectFile()
        self.type_uploadFile()
        #释放iframe，重新回到主页面上
        self.type_default_iframe()
        #关闭上传窗口
        time.sleep(10)
        self.type_notice()
        time.sleep(5)
        self.type_close()
        time.sleep(5)
        #保存
        self.type_submit()

        self.message_loc=(By.XPATH,'/html[1]/body[1]/div[8]/h2[1]')
    # 保存成功的情况
    def type_savePass_hint(self):
        time.sleep(5)
        return self.find_element(*self.message_loc).text



