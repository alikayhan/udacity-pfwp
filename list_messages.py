#!/usr/bin/env python3

__author__ = 'alikayhan'

from twilio.rest import TwilioRestClient

# Put your own credentials here
ACCOUNT_SID = "your_account_sid"
AUTH_TOKEN = "your_auth_token"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

messages = client.messages.list(
)


def list_messages(message_list):
    for m in message_list:
        print(m.sid)
        message = client.messages.get(m.sid)
        print(message.body + "\n")


list_messages(messages)

