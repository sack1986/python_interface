from BSTestRunner import BSTestRunner
import unittest
import time
from  test_case.model.function import *

report_dir = './test_report'
test_dir = './test_case'
print("start run testcase...")
#discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_practitioner.py')
#discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_comany.py')
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + ' resule.html'
print('Start write report...')
# 运行前记得把BSTestRunner.py 120行‘unicode'换成’str'
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='测试报告', description='资质系统登录测试')
    runner.run(discover)
f.close()

#发送邮件
# # 查找最新的测试报告
# print("find latest report...")
# latest_report = latest_report(report_dir)
# # 邮件发送报告
# print("send email report...")
# send_email(latest_report)
# print("test end!")


# mySuite=unittest.TestSuite()
    # mySuite.addTest(SearchTest("test_myCase1"))
    # mySuite.addTest(SearchTest("test_myCase2"))
    # myRunner=unittest.TextTestRunner()
    # myRunner.run(mySuite)
