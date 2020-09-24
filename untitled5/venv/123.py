
from selenium import webdriver
import os
import time


def browser():
    #driver=webdriver.Firefox()
    #driver = webdriver.Chrome()
    driver=webdriver.Ie()
    return driver



def insert_img(filename):
     # 将路径转换成相对路径
     func_path = os.path.dirname(__file__)  # 获取当前模块目录的路径
     base_dir = os.path.dirname(func_path)  # 获取当前模块目录的上一级目录的路径
     base_dir = str(base_dir)
     base_dir = base_dir.replace('\\', '/')
     base = base_dir.split('/Website')[0]
     nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
     filepath = u"D:\\Users\\Administrator\\PycharmProjects\\untitled\\venv\\fdczzxt_test\\Website\\test_report\\screemshot\\"+nowtime+'.png'
     filepath = base + '/Website/test_report/screenshot/' + filename


     print(filepath )


    #filepath=u"D:\\Users\\Administrator\\PycharmProjects\\untitled\\venv\\fdczzxt_test\\Website\\test_report\\screemshot\\"
    #driver.get_screenshot_as_file(filepath+filename)


if  __name__=="__main__":

    insert_img('123.jpg')