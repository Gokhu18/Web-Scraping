# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:04:35 2019

@author: Vishal Tyagi
"""

#from selenium import webdriver
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import os
os.chdir("D:\\ketsaal data\\scraping")

myurl="https://www.flipkart.com/search?q=washing%20machine%20cover&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
uclient=uReq(myurl)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,"html.parser")
container=page_soup.find_all("div",{"data-id":"ALCECCMEGYCZYGAM"})
containers=container[0]
print(len(container))
print(soup.prettify(container[0]))
print(containers.div.img["alt"])  # title name

#Name=containers.find('a', attrs={'class':'_2cLu-l'})
#price=containers.find('div', attrs={'class':'_1vC4OE'})
#print(Name.text)#_2cLu-l

#name=containers.find_all("div",{'title':'_2cLu-l'})
#
#price=containers.find_all("div",{"class":"_1vC4OE"})
#print(price[0].text)
#rating=containers.find_all("div",{"class":"hGSR34"})
#print(rating[0].text)
#Specification = containers.find_all("div",{"class":"_1rcHFq"})
#print(Specification[0].text)
#filename="products.csv"
#f=open(filename,"w")
#header="product_name,price,rating\n"
#f.write(header)
#for containers in container:
#    product_name=containers.div.img["alt"]
#    product_name.replace(",","|")
#    price_container=containers.find_all("div",{"class":"_1vC4OE"})
#    price=price_container[0].text.strip()
#    rating_container=containers.find_all("div",{"class":"hGSR34"})
#    rating=rating_container[0]
    
    
#print("product_name:" + product_name)    
#print("price"+price)
#print("rating: "+rating)

#flipa = pd.DataFrame(container)
#flipa.to_excel('flipa.xlsx')
##string parsing
#trim_price="".join(price.split(","))
#rm_rupee=trim_price.split("₹")
#add_rm_price="rs"+rm_rupee[1]
#split_price=add_rm_price.split("E")
#final_prices=split_price[0]
#split_rating=rating.split(" ")
#final_rating=split_rating[0]
#print(product_name.replace(",","|") + final_prices + ","+ final_rating +"\n" )
#
#product_name = product_name.replace(",","|")
#pdoductlist = pd.DataFrame({})

## Connect to the URL
#import urllib.request
#import requests
#from bs4 import BeautifulSoup

#
#response=requests.get(myurl)
#
## Parse HTML and save to BeautifulSoup object¶
#
#soup = BeautifulSoup(response.text, "html.parser")
import bs4

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
specifications = []

for containers in page_soup.findAll("div",{"class":"_3liAhj"}):
#    name=containers.div.img["alt"]
    name=containers.find('a', attrs={'class':'_2cLu-l'})
    price=containers.find('div', attrs={'class':'_1vC4OE'})
    rating=containers.find('div', attrs={'class':'hGSR34'}) 
    specification = containers.find('div', attrs={'class':'_1rcHFq'})
    products.append(name.text) if type(name) == bs4.element.Tag  else products.append('NaN')
    prices.append(price.text)
    specifications.append(specification.text)
    ratings.append(rating.text) if type(rating) == bs4.element.Tag  else ratings.append('NaN')

type(name)

df = pd.DataFrame({'Product Name':products,'Price':prices, 'Rating':ratings,'specification':specifications}) 
df.to_excel('Washing Machine Cover.xlsx', index=False, encoding='utf-8')
