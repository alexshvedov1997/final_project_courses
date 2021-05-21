from .base_class_scrapper import AbstractScraper
#from compare_price.analize_site.classes.base_class_scrapper import AbstractScraper
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


class BelconsoleGameFind(AbstractScraper):

    def __init__(self, path):
        super(BelconsoleGameFind, self).__init__(path)

    def get_count_of_page(self):
        try:
            soup = BeautifulSoup(self.get_html(self.path), 'lxml')
            page_str = soup.find("div", class_="page-view col-sm-8 col-xs-12").find_all("a")
        except:
            return 7
        return int(page_str[-2].get_text())


    def new_func_get_all_data(self, html):
        dict_ = {}
        try:
            soup = BeautifulSoup(html, 'lxml')
            links = soup.find('div',
                              class_='col-md-9 col-sm-12 col-xs-12 main-content').\
            find_all('div', class_="product-description")
            for elem in links:
                name = elem.find('div', class_="product-name").find('a').get_text().strip()
                price = elem.find("div", class_="product-price").\
                    find("span", class_="current-price").get_text()
                dict_[name] = price
        except:
            dict_['None'] = ''
        return dict_


    def get_all_link_page(self, num):
        for elem in range(1, num + 1):
            str_ = self.path + "?page_num=" + str(elem)
            self.link_list.append(str_)


#obj_ = BelconsoleGameFind(r"https://www.belconsole.by/playstation_4/igry_dlya_ps4/")
#obj_.get_all_link_page(obj_.get_count_of_page())
#obj_.get_all_data()
#print(obj_.super_dict)
#print(obj_.find_game("Assassin's"))

