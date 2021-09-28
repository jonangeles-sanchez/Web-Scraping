from typing import Text
import requests
from bs4 import BeautifulSoup
import pandas
df = pandas.DataFrame(1)

r=request.get("https://www.century21.com/real-estate/mars-hill-nc/LCNCMARSHILL/")

c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

page_nr=soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr,"number of pages were found")

base_url="https://www.century21.com/real-estate/mars-hill-nc/LCNCMARSHILL/"
for page in range(0,int(page_nr)*10,10):
    print( )
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    #c=r.json()["list"]
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    
print(all)

l = [];

for item in all:
    d={}
    d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
    try:
        d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
    except:
        d["Locality"]=None
    d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
    d["Price"]=(item.find_all("span",{"class","propAddressCollapse"})[1])
    try:
        d["Beds"]=(item.find("span",{"class","infoBed"}).find("b").text)
    except:
        d["Beds"]=("Probably land estate")
        pass

    try:
        d["Area"]=(item.find("span",{"class","infoSqFt"}).find("b").text)
    except:
        d["Area"]=("Probably land estate")

    try:
        d["Full Baths"]=(item.find("span",{"class","infoValueFullBath"}).find("b").text)
    except:
        d["Full Baths"]=("Probably land estate")

    try:
        d["Half Baths"]=(item.find("span",{"class","infoValueHalfBath"}).find("b").text)
    except:
        d["Half Baths"]=("Probably land estate")
    for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=(feature_name.text)

l.append(d)
df.to_csv("Output.csv")