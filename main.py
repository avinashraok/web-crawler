#! /usr/bin/env python3.4

import requests
from bs4 import BeautifulSoup

url = "http://www.cricbuzz.com/"

req = requests.get(url)
print(req.status_code)
soup = BeautifulSoup(req.text)
d = (req.text).split(">")
#with open("data.txt","w") as f:
#  for i in d:
#    f.write(i + '\n')

for section in soup.find_all("div", {"class":"cb-ovr-flo"}):
  print(str(section.string))

