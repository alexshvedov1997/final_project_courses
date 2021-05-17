import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def get_all_name(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('section', id='products').find_all('h5', class_="product-name")
    list_ = []
    for elem in links:
        list_.append(elem.find('a').get_text())

    return list_

html_ = get_html(r"https://warp.by/igry-dlya-ps4?page=2")
link = get_all_name(html_)
print(*link, sep="\n")