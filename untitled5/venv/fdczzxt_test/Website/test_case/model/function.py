from selenium import webdriver
import os
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart  # 用于传送附件


def insert_img(driver, filename):
    # 将路径转换成相对路径
    func_path = os.path.dirname(__file__)  # 获取当前模块目录的路径
    base_dir = os.path.dirname(func_path)  # 获取当前模块目录的上一级目录的路径
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/Website')[0]
    #filepath = base + '/Website/test_report/screenshot/' + filename
    filepath = u"D:\\Users\\Administrator\\PycharmProjects\\untitled\\venv\\fdczzxt_test\\Website\\test_report\\screemshot\\"
    driver.get_screenshot_as_file(filepath+filename)












#发送邮件，有问题，需要修改
# def latest_report(report_dir):
#     # os.listdir()方法用于返回指定文件夹包含文件或文件夹的名字列表
#     lists = os.listdir(report_dir)
#     # 按照时间顺序对该目录文件夹下面的文件进行排序
#     lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
#     # 输出最新的报告路径
#     file = os.path.join(report_dir, lists[-1])
#     return file
#
#
# def send_email(latest_report):
#     with open(latest_report, 'rb') as e:
#         mail_content = e.read()
#     e.close()
#     # 发送邮箱服务器
#     smtpserver = 'smtp.qq.com'
#     # 发送邮件用户名和密码
#     user = 'daishaoli@163.com'
#     password = '3698914sack'  # 授权码作为密码
#     # 发送和接收的邮箱
#     sender = 'daishaoli@163.comm'
#     # receiver='9*********@qq.com'  #收件人是单个
#     receiver = ['414319054@qq.com', 'yotoamo@126.co']  # 收件人是多个
#     # 发送邮件主题和内容
#     subject = 'Web Selenium AutoTest Report by Flora.Chen'
#     # content='<html><h1 stype="color:red">Web Selenium AutoTest Report by Flora.Chen</h1></html>'
#     msgRoot = MIMEText(mail_content, 'html', 'utf-8')
#     msgRoot['Subject'] = Header(subject, 'utf-8')
#     msgRoot['From'] = sender
#     # msg['To']=receiver #收件人是单个
#     msgRoot['To'] = ','.join(receiver)  # 收件人是多个
#     # SSL协议端口号使用
#     smtp = smtplib.SMTP_SSL(smtpserver, 465)
#     # 向服务器标识用户身份
#     smtp.helo(smtpserver)
#     # 服务器返回结果确认
#     smtp.ehlo(smtpserver)
#     # 登录邮箱服务器用户名和密码
#     smtp.login(user, password)
#     print('开始发送邮件...')
#     smtp.sendmail(sender, receiver, msgRoot.as_string())
#     smtp.quit()
#     print('邮件发送结束')


