from django.shortcuts import render, get_object_or_404
from .models import ReviewGame
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def main_page_show(request):
    obj_list = ReviewGame.objects.all()
    paginator = Paginator(obj_list, 2)
    page = request.GET.get('page')
    try:
        obj_ = paginator.page(page)
    except PageNotAnInteger:
        obj_ = paginator.page(1)
    except EmptyPage:
        obj_ = paginator.page(paginator.num_pages)
    return render(request, "blog_page/main_page.html", {'page':page, 'list_review': obj_ })


def review_detail(request, slug):
    obj_ = get_object_or_404(ReviewGame, slug=slug)
    return render(request, "blog_page/detail_review.html", {'review_game': obj_})

# Create your views here.
