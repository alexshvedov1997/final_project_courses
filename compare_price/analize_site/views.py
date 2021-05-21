from django.shortcuts import render
from .classes.manager_web import ManagerWebPage
from datetime import datetime



def controler_two_price(request):
    if request.method == "POST":
        name_ = request.POST["game_name"]
        start_time = datetime.now()
        elem = ManagerWebPage.find_game_warp(name_)
        elem_2 = ManagerWebPage.find_game_belconsole(name_)
        end = datetime.now()
        print("Время выполнения: {}".format(end - start_time))
        return render(request, "scraper_page/scrap_site.html", {"elem": elem, "elem_2" : elem_2})
    return render(request, "scraper_page/form_find_game.html")

# Create your views here.
