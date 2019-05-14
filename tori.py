from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.tori.fi/koko_suomi/vaatteet_ja_kengat?ca=18&q=adidas%20boost&cg=3050&st=s&cs=2&w=3&ck=16"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"desc"})

filename = "torikengät_boost.csv"
f = open(filename, "w")

headers = "KENKÄ, HINTA\n"

f.write(headers)

for container in containers:
    kenkä = container.a.text
    
    hinta_container = container.findAll("p", {"class":"list_price"})
    hinta = hinta_container[0].text


    f.write(kenkä.replace(",", "/") + "," + hinta + "\n")

    print("Valmis")

f.close