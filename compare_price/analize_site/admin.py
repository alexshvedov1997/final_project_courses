from django.contrib import admin
from  .models import WarpGames, BelconsoleGames

@admin.register(WarpGames)
class WarpGameAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(BelconsoleGames)
class BelconsoleGameAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']




