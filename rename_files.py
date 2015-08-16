__author__ = 'alikayhan'

import os
from string import digits


def rename_files():
    path = "/Users/alikayhan/Desktop/prank/"
    file_list = os.listdir(path)
    # print(file_list)
    for file_name in file_list:
        os.rename(path+file_name, path+file_name.translate(None, digits))

rename_files()




