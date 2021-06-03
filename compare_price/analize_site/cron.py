from .classes.game_handler import GameInformation
from django.db import connection


def add_to_games_bel_db(dict_):
    with connection.cursor() as cursor:
        for key, value in dict_.items():
            cursor.execute("""INSERT INTO analize_site_belconsolegames VALUES(%s, %s)
            ON CONFLICT(name) DO UPDATE
            SET price = excluded.price""", [key, value[0]])

def add_to_games_warp_db(dict_):
    with connection.cursor() as cursor:
        for key, value in dict_.items():
            cursor.execute("""INSERT INTO analize_site_warpgames VALUES(%s, %s)
            ON CONFLICT(name) DO UPDATE
            SET price = excluded.price""", [key, value[0]])



def cron_add_games():
    games = GameInformation()
    add_to_games_warp_db(games.all_data_warp())
    add_to_games_bel_db(games.all_data_belconsole())

