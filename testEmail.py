#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
import requests
 


# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="user"    #用户名
mail_pass="pass"   #口令 
 
 
sender = ' '
receivers = [' ']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEMultipart()
message['From'] = sender

 
subject = '网络图片1'
message['Subject'] = Header(subject, 'utf-8')
message.attach(MIMEText('这是带网络图片附件的邮件……', 'plain', 'utf-8')) #正文
#message['Content'] = "e,zhe shi wod exin yo uxiang"

#附件下载并写入本地

imgurl="http://img0.dili360.com/ga/M02/02/18/wKgBzFQ2x9eAbZn8AATCSQolols997.jpg@!rw17"
file_att = 'E:\\Git\\test\\image_tmp.jpg'

imgre = requests.get(imgurl)
open(file_att, "wb").write(imgre.content)
print("下载完毕")


att1 = MIMEApplication(open(file_att, 'rb').read())
att1.add_header('Content-Disposition', 'attachment', filename= file_att.split('\\')[-1])
message.attach(att1)

####
#zipFile = '算法设计与分析基础第3版PDF.zip'
#zipApart = MIMEApplication(open(zipFile, 'rb').read())
#zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
###

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print ("邮件发送成功")
except smtplib.SMTPException as err:
    print (err)