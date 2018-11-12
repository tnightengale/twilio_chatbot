#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:08:57 2018

@author: tnightengale
"""

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_PATH']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create responses object to match responses SQLite table
class responses(db.Model):
    response_id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.String(300), unique=True, nullable=False)
    date = db.Column(db.String(120), unique=True, index=True, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    
    # database update
    incoming_number = request.values.get('From')
    incoming_response = request.values.get('Body')
    #time_stamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    
    
    incoming_resp = responses(
            number=incoming_number,body=incoming_response,
            date=datetime.utcnow())
    
    db.session.add(incoming_resp)
    db.session.commit()
    
    
    
    
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    
    
    
    
    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    
    if 'OPTION_1' in body:
       response = [
               'You chose option 1. Great choice!', 
               ]
    elif 'OPTION_2' in body:
        response = [
                'You chose option 2. Nice!'
                ]
    else:   
        response = [
                'You are texting an informational chatbot!',
                'For more information, about our offerings, reply',
                'with the keyword OPTION_1 OR OPTION_2.'
                ]
    
    response = ' '.join(response)
    
    #print(response) ## on local?
    
    resp.message(response)
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
