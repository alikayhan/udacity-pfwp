#!/usr/bin/env python3

# __author__ = 'alikayhan'

from twilio.rest import TwilioRestClient

account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Hello, dude!",
    to="+16282226242",
    from_="+16282226242"
)

print(message.sid)

