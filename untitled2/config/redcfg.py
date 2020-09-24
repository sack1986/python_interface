# coding:utf-8
import os
import configparser

cur_path=os.path.dirname(os.path.realpath(__file__))
configpath=os.path.join(cur_path,"cfg.ini")
conf=configparser.ConfigParser()
conf.read(configpath,encoding= 'utf-8')

#email信息
email_server=conf.get("email","smtpserver")
email_port=conf.get("email","port")
email_sender=conf.get("email","sender")
email_psw=conf.get("email","psw")
email_receiver=conf.get("email","receiver")


#database信息
host=conf.get("database","host")
user=conf.get("database","user")
pwd=conf.get("database","pwd")
db=conf.get("database","datadb")