from django.shortcuts import render, get_object_or_404, redirect
from .models import ReviewGame, CommentModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, SearchForm, ReviewForm
from django.contrib.postgres.search import SearchVector
from taggit.models import Tag
import analize_site.models as prj


def main_page_show(request, tag_slug=None):
    obj_list = ReviewGame.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        obj_list = obj_list.filter(tags__in=[tag])
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
                                                        "search_form" : search_form, 'tag':tag})


def review_detail(request, slug):
    obj_ = get_object_or_404(ReviewGame, slug=slug)
    new_comment = None
    comment_form = None
    comment_list = CommentModel.objects.filter(post=obj_)
    game_name= prj.WarpGames.objects.annotate(
        search=SearchVector('name'),
    ).filter(search=obj_.title)
    game_warp= []
    game_belconsole = []
    for elem in game_name:
        game_warp.append(prj.WarpGames.objects.filter(name=elem))
    game_name = prj.BelconsoleGames.objects.annotate(
        search=SearchVector('name'),
    ).filter(search=obj_.title)
    for elem in game_name:
        game_belconsole.append(prj.BelconsoleGames.objects.filter(name=elem))

    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid:
                new_comment = comment_form.save(commit=False)
                new_comment.author = request.user
                new_comment.post = obj_
                new_comment.save()
        else:
            comment_form = CommentForm()
    return render(request,
                  "blog_page/detail_review.html",
                  {'review_game': obj_,
                   "comment_form": comment_form,
                   'comments': comment_list, 'game_warp':game_warp,
                   "game_belconsole":game_belconsole})


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
    return render(request, 'blog_page/search_results.html', {'res': res})


def create_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.author = request.user
            new_review.save()
            return  redirect('blog:main_pg')
    new_form = ReviewForm()
    return render(request, "blog_page/create_review.html", {"new_form": new_form})



# Create your views here.
