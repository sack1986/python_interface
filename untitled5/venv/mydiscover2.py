
import unittest
import HTMLTestRunner
import time

def create_suite(testcase_dir):
    """创建测试套件"""
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_dir, "tst*.py")
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTest(test_case)
    return suite

def run(suite):
    """运行测试套件"""
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # filename = "E:\\myTestCase\\Reports\\Results-" + now + "result.html"
    # print(filename)
    # fp = open("E:\\myTestCase\\Reports\\Results-" + now + "result.html", 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Result', description='Test_Report')
    # runner.run(suite)
    # print('Test reports generate finished')

    report_path = "E:\\myTestCase\\Reports\\result.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = "自动化测试unittest测试框架报告",description = "用例执行情况：")
    runner.run(suite)
    fp.close()

if __name__ == "__main__":
    case_dirs = r"E:\myTestCase"
    # 创建测试套件
    suite = create_suite(case_dirs)
    # 运行测试用例
    run(suite)

