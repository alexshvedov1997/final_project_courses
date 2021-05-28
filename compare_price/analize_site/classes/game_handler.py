from .warp_ps4 import WarpGameFind
from .belconsole_ps4 import BelconsoleGameFind

class GameInformation:

    def __init__(self):
        self._game1 = WarpGameFind(r"https://warp.by/igry-dlya-ps4")
        self._game1.get_all_link_page(self._game1.get_count_of_page())
        self._game1.get_all_data()
        self._game2 = BelconsoleGameFind(r"https://www.belconsole.by/playstation_4/igry_dlya_ps4/")
        self._game2.get_all_link_page(self._game2.get_count_of_page())
        self._game2.get_all_data()

    def all_data_warp(self):
        return self._game2.super_dict

    def all_data_belconsole(self):
        return self._game1.super_dict