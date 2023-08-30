import requests
from bs4 import BeautifulSoup

print("====================")

def get_page_links(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'html.parser')
    #print("sp #", sp)
    #links = sp.select('li')
    links = sp.select('li a')
    print("Link # ", links)
    print(sp("product-grid__item"))

#get_page_links('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?viewType=listing&limit=72')
#get_page_links('https://www.thewhiskyexchange.com/specialoffers')
get_page_links('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')