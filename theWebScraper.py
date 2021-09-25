import requests
from bs4 import BeautifulSoup

r=request.get("https://www.century21.com/real-estate/mars-hill-nc/LCNCMARSHILL/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div", {"class":"propertyRow"})

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

for item in all:
    print(item.find ("h4",{"class","propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class","propAddressCollapse"})[0])
    print(item.find_all("span",{"class","propAddressCollapse"})[1])