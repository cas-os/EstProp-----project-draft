import requests
from bs4 import BeautifulSoup

print("====================")

def get_page_links(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    links = sp.select('li.listing-item a')
    print(links)

get_page_links('http://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?viewType=listing&limit=72')