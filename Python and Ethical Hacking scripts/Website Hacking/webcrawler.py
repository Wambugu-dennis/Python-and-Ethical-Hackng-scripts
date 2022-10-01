#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "test.com"
subdomains_list = ""
directories_list = ""
final_url = ""
# with open("/dir*/path*/subdomains-wordlist.txt", "r") as subdomain_file:
with open("/dir*/path*/files-and-dirs-wordlist.txt", "r") as directory_file:
    print("[+] ----- Discovered Valid subdomain(s) and Valid directories -----   ")

    # discovering subdomains
    # for sub_line in subdomain_file:
    #     word = sub_line.strip()
    #     test_url = word + "." + target_url
    #     sub_response = request(test_url)
    #  discovering directories
    for dir_line in directory_file:
        directory = directory_file.readline()
        test_dir = target_url + "/" + directory
        dir_response = request(test_dir)

    # if sub_response:
    #     subdomains_lists = subdomains_list + test_url
        if dir_response:
            directories_list = directories_list + test_dir
            final_url = sub_response + dir_response
            print(directories_list)

