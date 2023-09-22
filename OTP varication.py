# Importing modules
import random
import smtplib

#generating a randomm 6-digit OTP
OTP = random.randint(100000,999999)      

#setting up server
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

#IP address of smtp.gmail.com to bypass DNS resolution
name = input("enter your name:")
global receiver_email
receiver_email = input("enter your email id:")

def email_verification(receiver_email):
    email_check1 = ["gmail","hotmail","yahoo","outlook"]
    email_check2 = [".com",".in",".org",".edu",".co.in"]
    count = 0

    for domain in email_check1:
        if domain in receiver_email:
            count+=1
    for site in email_check2:
        if site in receiver_email:
            count+=1

    if "@" not in receiver_email or count!=2:
        print("invalid email id")
        new_receiver_email = input("enter correct email id:")
        email_verification(new_receiver_email)
        return new_receiver_email
    return receiver_email

valid_receiver_email = email_verification(receiver_email)
password = "owgo wxgk zzkw lfwr"
server.login("otpvarication@gmail.com",password)

body = "dear"+name+","+"\n"+"\n"+"your OTP is "+str(OTP)+"."
subject = "verification number using python"
message = f'subject:{subject}\n\n{body}'

server.sendmail("otpvarication@gmail.com",valid_receiver_email,message)

def sending_otp(receiver_email):
    new_otp = random.randint(100000,999999)

    body = "dear"+name+","+"\n"+"\n"+"your verification number is "+str(new_otp)+"."
    subject = "verification number using python" 
    message = f'subject:{subject}\n\n{body}'
    server.sendmail("otpvarication@gmail.com",receiver_email,message)
    print("verification number has been sent to"+receiver_email)
    received_OTP = int(input("enter number:"))

    if received_OTP==new_otp:
        print("number verified")
    else:
        print("invalid number")
        print("resending number.....")
        sending_otp(receiver_email)
    
print("number has been sent to "+valid_receiver_email)
received_OTP = int(input("enter number:"))

if received_OTP==OTP:
    print("number verified")
else:
    print("invalid number")
    answer = input("enter yes to resend number on same email and no to enter a new email id:")
    YES = ['YES','yes','Yes']
    NO = ['NO','no','No']
    if answer in YES:
        sending_otp(valid_receiver_email)
    elif answer in NO:
        new_receiver_email = input("enter new email id:")
        email_verification(new_receiver_email)
        sending_otp(new_receiver_email)
    else:
        print("invalid input")

server.quit()