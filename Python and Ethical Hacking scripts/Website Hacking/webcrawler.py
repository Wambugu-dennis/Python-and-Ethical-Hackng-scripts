#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "vulnerableweb.com"
subdomains_list = ""
directories_list = ""
final_url = ""
with open("/directory*/path*/subdomains-wordlist.txt", "r") as sub_file:
    with open("/directory*/path*/subdomains-wordlist.txt", "r") as dir_file:

        print("[+] ----- Discovered Valid subdomain(s) and directories -----   ")
        for sub_line in sub_file:
            sub_d = line.strip()
            test_url = sub_d + "." + target_url
            sub_response = request(test_url)

            for dir_line in dir_file:
                dir_d = line.strip()
                test_dir = target_url + "/" + dir_d
                dir_response = request(test_url)

            if sub_response and dir_response:
                final_url = subdomains_list + directories_list
                print(final_url)

