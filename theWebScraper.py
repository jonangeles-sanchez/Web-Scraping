import requests
from bs4 import BeautifulSoup

r=request.get("https://www.century21.com/real-estate/mars-hill-nc/LCNCMARSHILL/")
c=r.content

soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())