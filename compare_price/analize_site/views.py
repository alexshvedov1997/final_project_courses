from django.shortcuts import render
from .classes.warp_ps4 import WarpGameFind
from .classes.belconsole_ps4 import BelconsoleGameFind


def controler_two_price(request):
    obj_ = WarpGameFind(r"https://warp.by/igry-dlya-ps4")
    obj_.get_all_link_page(obj_.get_count_of_page())
    obj_.get_all_data()
    elem = obj_.find_game("Assassin's")
    obj_2 = BelconsoleGameFind(r"https://www.belconsole.by/playstation_4/igry_dlya_ps4/")
    obj_2.get_all_link_page(obj_2.get_count_of_page())
    obj_2.get_all_data()
    elem_2 = obj_2.find_game("Assassin's")
    return render(request, "scraper_page/scrap_site.html",{"elem": elem , "elem_2" : elem_2})

# Create your views here.
