import math
import random
import smtplib
from twilio.rest import Client
import sms
# Generate OTP 
def GenerateOTP():
    digits = "0123456789"
    length = len(digits)
    otp = ""

    for i in range(6):
        otp += digits[math.floor(random.random()*length)]

    return otp
# validate the mobile number
def ValidateMobile(PhoneNo):
     if len(PhoneNo) != 10:
        print("Please enter valid Mobile number!!")
        PhoneNo = input("Enter the number:")
     return PhoneNo
#validate the emailid
def ValidateEmailID(Email):
    if "@gmail.com" not in Email:
        print("Please Enter Valid Email address!!")
        Email = input("Enter the Email:")
    return Email
# send OTP to input mobile number
def sendOTPOverMobile(PhoneNo2, OTP):
    client = Client(sms.account_sid, sms.auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+OTP,

        from_=sms.twilio_number,
        to='+91'+str(PhoneNo2),
    )
    print(Message.body)
# send OTP to input emailid
def sendOTPOverEmail(Email2, OTP):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  
    server.login('naikatharva111@gmail.com', 'jbctzddvhpwysdhf')
    message = 'Your 6 digit OTP is '+str(OTP)
    server.sendmail('naikatharva111@gmail.com',
                    Email2, message)
    server.quit()



PhoneNo = input("Enter the number:")
PhoneNo2 = ValidateMobile(PhoneNo)

Email = input("Enter the Email:")
Email2 = ValidateEmailID(Email)

OTP = GenerateOTP()

sendOTPOverMobile(PhoneNo2, OTP)

sendOTPOverEmail(Email2, OTP)
