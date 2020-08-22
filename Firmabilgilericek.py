#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pyt"
)
mycursor = mydb.cursor()


def cek(qq):
    url="http://www.isfirmarehberi.com/firma/"+str(qq)
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    soup.prettify()
    linkler=soup.find_all("td")
    a=0
    b=""
    for link in linkler:
        a=a+1
        if link.text!=":":
            if (a%3!=1):
                b=b+link.text+"şşş"
            
                print(link.text)
                #print("asdasdasdşşş".split('şşş')[0])
    sql = "INSERT INTO firmalar (ad) VALUES ('"+b+"')"

    print("Kayıt Edildi:"+str(qq))
    mycursor.execute(sql)

    mydb.commit()
            


for i in range(5000,10000):
    cek(i)