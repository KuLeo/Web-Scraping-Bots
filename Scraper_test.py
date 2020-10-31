#!/usr/bin/python3 -u

import requests

from bs4 import BeautifulSoup


url = 'https://www.ebay.co.uk/itm/Uncirculated-1926-Philadelphia-Mint-\
    Silver-Peace-Dollar/352882650405?hash=item522971ed25:g:CiAAAOSw5LRd7E2M'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="itemTitle").get_text()
price = soup.find(id="prcIsum_bidPrice").get_text()


print(title.strip())
print(price.strip())
