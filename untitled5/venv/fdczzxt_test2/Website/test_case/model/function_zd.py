from selenium import webdriver
import os
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart  # 用于传送附件
from driver.driver import *
import time


class Screen(object):

    def __init__(self,driver,filename):
        self.driver = driver
        self.filename=filename


    def __call__(self, func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                filepath = "D:\\Users\\Administrator\\PycharmProjects\\untitled\\venv\\fdczzxt_test2\\Website\\test_report\\screemshot\\"+ self.filename
                self.driver.get_screenshot_as_file(filepath)
                raise

        return inner

