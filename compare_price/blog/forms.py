from django import forms
from .models import CommentModel, ReviewGame


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('body',)


class SearchForm(forms.Form):
    query = forms.CharField(label="Поиск рецензии")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewGame
        fields = ['title', 'slug', 'body', 'image', 'tags']