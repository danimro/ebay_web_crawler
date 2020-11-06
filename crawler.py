from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import sympy

#
primes = list(sympy.primerange(1111111111, 2147483647))
links = []
for prime in primes:
    if (prime % 10) == int(prime / 1000000000):
        links.append("https://www.ebay.com/p/" + str(prime))
#print(relevant_primes)

#links = ["https://www.ebay.com/p/1104956473", "https://www.ebayinc.com/riddle/1111110971"]

for link in reversed(links):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        webpage = urlopen(req)
    except HTTPError as e:
        continue
    with requests.Session() as c:
        print(link)
        break
        #soup = BeautifulSoup(webpage.read(), 'html5lib')
        #print(soup.findAll("div", attrs={"class": "s-value"})[3].text)
