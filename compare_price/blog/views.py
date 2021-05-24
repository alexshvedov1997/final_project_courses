from django.shortcuts import render, get_object_or_404
from .models import ReviewGame, CommentModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, SearchForm
from django.contrib.postgres.search import SearchVector


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
    search_form = SearchForm

    return render(request, "blog_page/main_page.html", {'page':page, 'list_review': obj_ ,
                                                        "search_form" : search_form})


def review_detail(request, slug):
    obj_ = get_object_or_404(ReviewGame, slug=slug)
    new_comment = None
    comment_form = None
    comment_list = CommentModel.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid:
                new_comment = comment_form.save(commit=False)
                new_comment.author = request.user
                new_comment.save()
        else:
            comment_form = CommentForm()
    return render(request,
                  "blog_page/detail_review.html",
                  {'review_game': obj_,
                   "comment_form": comment_form,
                   'comments': comment_list})


def search_handler(request):
    query = None
    res = []
    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            print("QUery2", query)
            res = ReviewGame.objects.annotate(
                search=SearchVector('title'),
            ).filter(search=query)
            print("res", res)
    return render(request, 'blog_page/search_results.html', {'res': res })

# Create your views here.
