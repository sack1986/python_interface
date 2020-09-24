from selenium import webdriver


'''
class SearchTest():


    def mytest(self):

        # webdriver.Ie("D:\Python36\IEDriverServer.exe")
        driver=webdriver.Ie()
        # webdriver.chrome()
        # driver.maximize_window()
        # driver.implicitly_wait(8)
        driver.get("https://www.baidu.com")




class SearchTest():
    #类方法不需要初始化实例
    @classmethod
    def mytest(cls):
        print("12")

SearchTest.mytest()
'''
class SearchTest():
    # 普通方法需要初始化对象，如果不初始化对象，无法调用

    def mytest(self,id):
        print(id)

a=SearchTest()
a.mytest(10)











