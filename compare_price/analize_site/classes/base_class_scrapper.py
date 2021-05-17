from abc import ABC, abstractmethod
import requests
from multiprocessing import Pool

class AbstractScraper(ABC):

    def __init__(self, path):
        self.link_list = []
        self.path = path
        self.list_dict = {}
        self.super_dict = {}

    def get_html(self, path):
        response = requests.get(path)
        return response.text

    @abstractmethod
    def new_func_get_all_data(self, html):
        pass

    @abstractmethod
    def get_count_of_page(self):
        pass

    def wrapper_func(self, url):
        return self.new_func_get_all_data(self.get_html(url))

    def get_all_link_page(self, num):
        for elem in range(1, num + 1):
            str_ = self.path + "?page=" + str(elem)
            self.link_list.append(str_)

    def create_super_dict(self):
        for d in self.list_dict:
            for k, v in d.items():
                self.super_dict.setdefault(k, []).append(v)


    def get_all_data(self):
        with Pool(60) as p:
            self.list_dict = p.map(self.wrapper_func, self.link_list)
            self.create_super_dict()


    def find_game(self, name_):
        lst_ = []
        lst_with_dict = []
        for key_ in self.super_dict.keys():
            if name_ in key_:
                lst_.append(key_)
        if lst_:
            for elem in lst_:
                lst_with_dict.append({elem : self.super_dict[elem][0]})
            return lst_with_dict
        return "Ничего не найдено"


