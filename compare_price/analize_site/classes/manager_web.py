from .warp_ps4 import WarpGameFind
from .belconsole_ps4 import BelconsoleGameFind


class ManagerWebPage:

    @staticmethod
    def find_game_warp(name):
        obj_ = WarpGameFind(r"https://warp.by/igry-dlya-ps4")
        obj_.get_all_link_page(obj_.get_count_of_page())
        obj_.get_all_data()
        return obj_.find_game(name)

    @staticmethod
    def find_game_belconsole(name):
        obj_ = BelconsoleGameFind(r"https://www.belconsole.by/playstation_4/igry_dlya_ps4/")
        obj_.get_all_link_page(obj_.get_count_of_page())
        obj_.get_all_data()
        return obj_.find_game(name)
