from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request(
    url='https://www.hepsiemlak.com/istanbul-besiktas-ulus-kiralik/daire/31303-139860', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
attrs= soup.find_all('li',class_="spec-item")

print(attrs)
print(len(attrs))