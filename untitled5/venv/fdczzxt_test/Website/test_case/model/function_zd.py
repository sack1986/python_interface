from selenium import webdriver
import os
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart  # 用于传送附件
from driver.driver import *


def insert_img(driver, filename):

    def __init__(self):
        self.driver = driver
        self.filename = filename

    def __call__(self, func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                filepath = u"D:\\Users\\Administrator\\PycharmProjects\\untitled\\venv\\fdczzxt_test\\Website\\test_report\\screemshot\\"
                driver.get_screenshot_as_file(filepath + filename)
                raise

        return inner

