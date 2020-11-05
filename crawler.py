from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

link = "https://www.ebay.com/p/1104956473"

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    print(soup.findAll("div", attrs={"class": "s-value"})[3].text)
