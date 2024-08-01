import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=realme&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
name=[]
for i in name[0:20]:
    d=i.get_text()
    name.append(d)
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
rates=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in rates[0:20]:
    d=i.get_text()
    rate.append(d)
images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
offers=soup.find_all('div',class_='_3Ay6Sb')
offer=[]
for i in offers[0:20]:
    d=i.get_text()
    offer.append(d)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
df=pd.DataFrame()
df["Names"]=name
df["Prices"]=price
df["Ratings"]=rate
df["Images"]=image
df["Offers"]=offer
df["Links"]=link
df.to_csv("Realme mobiles.csv")