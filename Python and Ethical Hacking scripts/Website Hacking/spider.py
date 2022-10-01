#!/usr/bin/env python

import requests
import re


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "zsecurity.org"
response = request(target_url)
href_links = re.findall('(?:href=")(.*?)"', response.content.decode())

print("\n[+] ----- Discovered links -----\n\n" + str(href_links))

