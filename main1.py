import math
import random
import smtplib
from twilio.rest import Client
import sms
from generate_otp import GenerateOTP
from validate_mobile_no import ValidateMobile
from validate_email_id import ValidateEmailID
PhoneNo = input("Enter the number:")
Email = input("Enter the Email:")
# Generate OTP 
GenerateOTP()
# validate the mobile number
ValidateMobile(PhoneNo)
#validate the emailid
ValidateEmailID(Email)
# send OTP to input mobile number
PhoneNo2 = ValidateMobile(PhoneNo) 
def sendOTPOverMobile(PhoneNo2, OTP):
    client = Client(sms.account_sid, sms.auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+OTP,

        from_=sms.twilio_number,
        to='+91'+str(PhoneNo2),
    )
    print(Message.body)
# send OTP to input emailid
Email2 = ValidateEmailID(Email)
def sendOTPOverEmail(Email2, OTP):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  
    server.login('naikatharva111@gmail.com', 'jbctzddvhpwysdhf')
    message = 'Your 6 digit OTP is '+str(OTP)
    server.sendmail('naikatharva111@gmail.com',
                    Email2, message)
    server.quit()







OTP = GenerateOTP()

sendOTPOverMobile(PhoneNo2, OTP)

sendOTPOverEmail(Email2, OTP)
