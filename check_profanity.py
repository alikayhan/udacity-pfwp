#!/usr/bin/env python3

__author__ = 'alikayhan'

import urllib.request

quotes_list = ""

def read_text():
    file = open(input("Enter the path of the text file to be checked for profanity: "))
    quotes_list = file.read()
    return quotes_list
    file.close()

def check_profanity(word_to_check):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q=" + urllib.parse.quote(word_to_check))
    output = connection.read()
    if "true" in str(output):
        print("Profanity Alert!")
    elif "false" in str(output):
        print("Clear!")
    else:
        print("Check process failed! Try again.")
    connection.close()

quotes_list = read_text()
check_profanity(quotes_list)
