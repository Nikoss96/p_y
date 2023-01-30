import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request

f = urllib.request.urlopen("https://www.wildberries.ru/promotions/sokolov?sort=rate&page=1&bid=77060f0c-6b70-47b4-8f55-ce313f3254f5&cardsize=c516x688#c10199477").read()
print(f)
baseurl = "https://www.wildberries.ru"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
URL_TEMPLATE = "https://www.wildberries.ru/promotions/sokolov?sort=rate&page=1&bid=77060f0c-6b70-47b4-8f55-ce313f3254f5&cardsize=c516x688#c10199477"
r = requests.get(URL_TEMPLATE)
print(r.status_code)
#f = urllib.urlopen("https://www.wildberries.ru/promotions/sokolov?sort=rate&page=1&bid=77060f0c-6b70-47b4-8f55-ce313f3254f5&cardsize=c516x688#c10199477")
#print(r.text)
soup = bs(r.text, "html.parser")
names = soup.find_all("ins",{"class":"price__lower-price"})
for name in names:
    print(name)