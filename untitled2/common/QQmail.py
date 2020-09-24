# coding:utf-8
import smtplib
from email.mime.text import MIMEText
# ----------1.跟发件相关的参数------
# smtpserver = "smtp.163.com" # 发件服务器
smtpserver = "smtp.qq.com"
port = 465 # 端口
sender = "414319054@qq.com" # 账号
psw = "kekwqnxgvhzlbgjc" # 密码
receiver = "daishaoli@163.com" # 接收人
# ----------2.编辑邮件的内容------
subject = "这个是主题 QQ"
body = '<p>这个是发送的 QQ 邮件</p>' # 定义邮件正文为 html 格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "283340479@qq.com"
msg['subject'] = subject
# ----------3.发送邮件------
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver) # 连服务器
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw) # 登录
smtp.sendmail(sender, receiver, msg.as_string()) # 发送
smtp.quit()