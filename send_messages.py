#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:35:15 2018

@author: tnightengale
"""
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import csv
import os


# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
client = Client(account_sid, auth_token)


def main():
    '''
    Main function looks for a file called recipients.csv
    in the directory with names in column 1 
    and numbers to text in column 2. It adds these
    names to dictionary "recipents". It sends 
    the message typed in message.txt to the numbers in the
    "recipients" dictionary.
    '''
    with open('recipients.csv','r') as f:
        stuff = csv.reader(f,dialect='excel')
            
        recipients = {}
        for r in stuff:
            r = r[0].split('\t')
            
            # assert names and numbers
            assert(len(r) == 2)
            
            # add name to dict
            recipients[r[0]] = r[1]
    
    with open('message.txt','r') as m:
        message_text = m.read()
        
        for name in recipients:
            message = client.messages \
                .create(
                     body=message_text,
                     from_=twilio_number,
                     to='+' + recipients[name]
                 )
            
            print(message.sid)
        
if __name__ == '__main__':
    main()