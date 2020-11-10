from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

dest_url = "https://www.tori.fi/koko_suomi?q=jordan+1&cg=0&w=3&st=s&st=g&ca=18&l=0&md=th"

uClient = uReq(dest_url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close

containers = page_soup.findAll("div", {"class":"desc_flex"})

filename = "torikengät.csv"
f = open(filename, "w")

headers = "KENKÄ, HINTA\n"

f.write(headers)

for container in containers:
    kenka_container = container.findAll("div", {"class":"li-title"})
    kenka = kenka_container[0].text
    
    hinta_container = container.findAll("p", {"class":"list_price"})
    hinta = hinta_container[0].text


    f.write(kenka.replace(",", "/") + "," + hinta + "\n")

f.close
print("Valmis")