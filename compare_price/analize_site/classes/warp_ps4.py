from .base_class_scrapper import AbstractScraper
#from compare_price.analize_site.classes.base_class_scrapper import AbstractScraper
import requests
from bs4 import BeautifulSoup

class WarpGameFind(AbstractScraper):

    def __init__(self, path):
        super(WarpGameFind, self).__init__(path)

    def get_all_name(self, html):
        list_ = []
        try:
            soup = BeautifulSoup(html, 'lxml')
            links = soup.find('section', id='products').find_all('h5', class_="product-name")
            for elem in links:
                list_.append(elem.find('a').get_text())
        except:
            list_.append('')
        return list_

    def new_func_get_all_data(self, html):
        dict_ = {}
        try:
            soup = BeautifulSoup(html, 'lxml')
            links = soup.find('section',
                              id='products').find_all('article',
                              class_="product-miniature product-style js-product-miniature")
            for elem in links:
                name = elem.find('h5', class_="product-name").find('a').get_text()
                price = elem.find("span", class_="price product-price").get_text()
                dict_[name] = price
        except:
            dict_['None'] = ''
        return dict_


    def get_count_of_page(self):
        soup = BeautifulSoup(self.get_html(self.path), 'lxml')
        page_str = soup.find("div", class_="pagination-wrapper light-box-bg clearfix")\
            .find_all("a", class_="js-search-link")
        return int(page_str[-2].get_text())

    def find_game(self, name_):
        lst_ = []
        lst_with_dict = []
        for key_ in self.super_dict.keys():
            if name_ in key_:
                lst_.append(key_)
        if lst_:
            for elem in lst_:
                str_ = self.__func_parse_price(self.super_dict[elem])
                lst_with_dict.append({elem : str_})
            return lst_with_dict
        return "Ничего не найдено"

    def __func_parse_price(self, lst_):
        str_ = lst_[0]
        pos = str_.find(" ")
        return str_[:pos - 1].strip() + " pуб."


#obj_ = WarpGameFind(r"https://warp.by/igry-dlya-ps4")
#obj_.get_all_link_page(20)
#obj_.get_all_data()
#print(obj_.super_dict)
#print(obj_.find_game("Farpoint"))



