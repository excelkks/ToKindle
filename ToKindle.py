#!/usr/local/bin/python3
import os
import getpass
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email地址和口令
from_addr = 'sender@email.com'  # input('From: ')
password = getpass.getpass('Password: ')
to_addr = 'acceipt@email.com'  # input('to: ')
# SMTP服务器地址
smtp_server = 'smtp-mail.outlook.com'  # input('SMTP server: ')
server = smtplib.SMTP(smtp_server, 25)  # 默认端口为25

# 加密
server.starttls()
# 登录
bLogin = False
while not bLogin:
        try:
                server.login(from_addr, password)
                bLogin = True
        except smtplib.SMTPAuthenticationError:
                password = getpass.getpass('Invalid Password ReEnter: ')


msg = MIMEMultipart()
msg["Subject"] = "e-book"
msg["From"] = from_addr
msg["To"] = to_addr

# 电子书格式
bookformat = ('.AZW3','.AZW','.TXT','.PDF','.MOBI','.HTML','.DOC','.DOCX','.JPEG','.GIF','.PNG','.BMP',
'.azw3','.azw','.txt','.pdf','.mobi','.html','.doc','.docx','.jpeg','.gif','.png','.bmp')


curr_dir = os.path.dirname(os.path.realpath(__file__))  # 当前目录
curr_dir_file = os.listdir(curr_dir)  # 当前目录中的文件
bkup_dir_name = curr_dir+'/'+'backup'  # 备份文件目录
# 创建备份目录
if not os.path.exists(bkup_dir_name):
        os.mkdir(bkup_dir_name)
# 将当前目录所有的电子书格式的文件attach到msg
for send_file_name in curr_dir_file:
    if send_file_name.endswith(bookformat):
        file_dir_name = curr_dir + '/'+send_file_name
        f = open(file_dir_name, 'rb')
        mime = MIMEApplication(f.read())
        f.close()
        mime.add_header('Content-Disposition', 'attachment', filename=send_file_name)
        msg.attach(mime)
        shutil.move(file_dir_name,bkup_dir_name+'/'+send_file_name)

# 发送
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
