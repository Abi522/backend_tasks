
import codecs

from django.core.mail import send_mail

from django.conf import settings

from .models import User
#from pyotp import otp
import sys
import smtplib
import pandas as pd


def send_otp_via_email(email):
    your_email = "abirami7094112264@gmail.com"
    your_password = "ylxelbrfnqhteyxm"
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)

    subject = "your account verification email"


    # establishing connection with gmail



    email_list = pd.read_excel('/home/lenovo/ecg/pythonProject4/email.xlsx')

        #print(email_list.read())

    # getting the zzzzzzz and the emails
    names = email_list['NAME']
    emails = email_list['EMAIL']

    # iterate through the records
    for i in range(len(emails)):
        # for every record get the name and the email addresses
        name = names[i]
        email = emails[i]

        # the message to be emailed
        message = "Hello " + name
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email])
        #user_obj = User.objects.get(email=email)
       # user_obj.save()
        server.close()







