from django.contrib import admin
from .models import ReviewGame
from django.utils.html import mark_safe

# Register your models here.

@admin.register(ReviewGame)
class AdminReviewGame(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'get_image', 'publish']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    list_filter = ('author', 'publish')
    ordering = ('publish',)

    def get_image(self, obj):
        if(obj.image):
            return mark_safe("<img src = '{}' width = '50' />".format(obj.image.url))
        return None

    get_image.__name__ = "Изображение"

