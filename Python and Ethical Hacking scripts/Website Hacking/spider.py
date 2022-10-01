#!/usr/bin/env python

import requests
import re

target_url = "http://zsecurity.org"
def extract_links(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode())

href_links = extract_links(target_url)
print("\n[+] ----- Discovered links -----\n")
for link in href_links:
    print( str(link))

