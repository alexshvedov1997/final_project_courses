from django.urls import path, include
from .views import main_page_show, review_detail, search_handler, create_review

app_name = 'blog'

urlpatterns = [
    path("main_page/", main_page_show, name="main_pg"),
    path("detail_review/<slug:slug>/", review_detail, name="detail_review"),
    path("main_page/search_result/", search_handler, name="search_handler"),
    path('tag/<slug:tag_slug>/', main_page_show, name='post_list_by_tag'),
    path("create_review/", create_review, name='create_review')
]