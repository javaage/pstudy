# coding=utf-8
import smtplib
from email.mime.text import MIMEText
import time

def sendMail(subject,content):
  msg_from = 'hb_java@sina.com'  # 发送方邮箱
  passwd = 'Tangyc_123'  # 填入发送方邮箱的授权码
  msg_to = 'hb_java@sina.com'  # 收件人邮箱

  msg = MIMEText(content)
  msg['Subject'] = subject
  msg['From'] = msg_from
  msg['To'] = msg_to
  try:
    s = smtplib.SMTP_SSL("smtp.sina.com.cn", 465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")
  except s.SMTPException as e:
    print("发送失败", e)
  finally:
    s.quit()

if __name__=="__main__":
  sendMail("crontab",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


