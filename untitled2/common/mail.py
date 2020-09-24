# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import redcfg
# ----------1.跟发件相关的参数------
#smtpserver = "smtp.163.com" # 发件服务器
smtpserver =redcfg.email_server
#port = 0 # 163端口
port = redcfg.email_port # QQmail端口
sender = redcfg.email_sender # 账号
psw = redcfg.email_psw# 密码
receiver =redcfg.email_receiver # 接收人
print(smtpserver,port,sender,psw,receiver)
# ----------2.编辑邮件的内容------
# 读文件
file_path = "../report/2020-08-28 15_10_21 resule.html"
with open(file_path, "rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender # 发件人
#msg["to"] = receiver # 单人收件人
msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
msg["subject"] = "测试报告" # 主题
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)
# ----------3.发送163和qq邮件------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver) # 连服务器
    smtp.login(sender, psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw) # 登录
smtp.sendmail(sender, receiver, msg.as_string()) # 发送
smtp.quit()

