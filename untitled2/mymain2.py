'''
class MyTest():
    def test1(**para):
        n=para;
        print(n)
        print(n['name'])

    def test2(*para):
        for n in para:
            print(n)


    if __name__ == '__main__':
        print("第一次")
        test1(**{'name':'lisi','sex':'女'});
        print("第二次")
        test1(**{'name':'zhangsan'})
        print("测试*para")
        test2(*[1,2,3,4]);


import unittest;

def case():
    case_dir="C:\\Users\\test\\PycharmProjects\\untitled2\\case"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,'test*.py', top_level_dir=None)
    testcase.addTests(discover)
    print(testcase)

if __name__=='__main__':
    runner=unittest.TextTestRunner()
'''

# coding:utf-8
import unittest
import HTMLTestRunner
from BSTestRunner import BSTestRunner
import time


#单个和批量运行测试用例
def all_case():
    # 待执行用例的目录
    case_dir = './case'
    #case_dir="C:\\Users\\test\\PycharmProjects\\untitled2\\case"
    #批量运行测试用例
    #discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    #单个运行测试用例
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_login_myfdczzxt.py")
    # discover 方法筛选出来的用例，循环添加到测试套件中
    # discover 方法筛选出来的用例，循环添加到测试套件中

    # for test_suite in discover:
    # for test_case in test_suite:
    # testunit.addTests(test_case)
    # print(testunit)

    return discover


if __name__ == "__main__":
    # discover 方法筛选出来的用例，循环添加到测试套件中
    report_dir = './report'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + ' resule.html'
    fp=open(report_name,"wb")
    #runner = unittest.TextTestRunner()
    runner=BSTestRunner(stream=fp,title='我的测试报告',description='测试报告描述：')
    # run 所有用例
    runner.run(all_case())
    fp.close()
