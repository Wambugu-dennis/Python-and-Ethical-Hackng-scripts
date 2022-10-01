#!/usr/bin/env python

import requests
import re
import urllib.parse as urlparse


target_url = "https://cybershujaa.co.ke/"  # supply your own domain here
target_links = []
def extract_links(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

print("\n[+] ----- Discovered valid links and directories -----\n")
def crawl(url):
    href_links = extract_links(url)
    try:
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if target_url in link and link not in target_links:
                target_links.append(link)
                print( str(link))
                crawl(link)
    except KeyboardInterrupt:
        exit()

crawl(target_url)
