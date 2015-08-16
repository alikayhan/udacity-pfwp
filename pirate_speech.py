#!/usr/bin/env python3

__author__ = 'alikayhan'

import urllib.request

text_to_convert = ""


def read_text():
    file = open(input("Enter the path of the text file to be converted to pirate speech: "))
    quotes_list = file.read()
    return quotes_list
    file.close()


def check_profanity(text):
    connection = urllib.request.urlopen("http://isithackday.com/arrpi.php?text=" + urllib.parse.quote(text))
    output = connection.read()
    print(output)
    connection.close()

text_to_be_converted = read_text()
check_profanity(text_to_be_converted)

