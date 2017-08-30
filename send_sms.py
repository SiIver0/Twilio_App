#!/usr/bin/env python

__author__          = 'Noah Yoshida' 
__email__           = 'nyoshida@nd.edu'

'''
With help from https://www.youtube.com/watch?v=uzBRycRYsqw
This program will send a text message to a phone number when the function 'send_sms' is  called 
'''

def send_msg(my_msg):
    from twilio.rest import Client
    from credentials import account_sid, auth_token, my_cell, my_twilio

    client = Client(account_sid, auth_token)

    message = client.messages.create(
            to =    my_cell,
            from_ = my_twilio,
            body =  my_msg)



