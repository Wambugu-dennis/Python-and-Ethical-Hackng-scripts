#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"
subdomains_list = ""
with open("/your*/directory*/path*/subdomains-wordlist.txt", "r") as wordlist_file:
    print("[+] ----- Valid subdomain(s) -----   ")
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            subdomains_lists = subdomains_list + test_url
            print(subdomains_lists)

