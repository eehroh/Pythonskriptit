from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

my_url = "https://www.tori.fi/koko_suomi?q=adidas&cg=3050&w=3&st=s&cs=2&ck=16&csz=134&ca=18&l=0&md=th"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"desc"})

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