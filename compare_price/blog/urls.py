from django.urls import path, include
from .views import main_page_show, review_detail

app_name = 'blog'

urlpatterns = [
    path("main_page/", main_page_show, name="main_pg"),
    path("detail_review/<slug:slug>", review_detail, name="detail_review")

]