#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"
subdomains_list = ""
# directories_list = ""
with open("/home/bitsec/Downloads/files-and-dirs-wordlist.txt", "r") as wordlist_file:
    print("[+] ----- Valid subdomain(s) -----   ")

    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        # for discovering directories
        # test_dir = target_url + "/" + word
        # response = request(test_dir)

        if response:
            # for subdomains
            subdomains_lists = subdomains_list + test_url
            print(subdomains_lists)
            # for directories
            # directories_list = directories_list + test_dir
