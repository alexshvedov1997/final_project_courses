from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from taggit.managers import TaggableManager


class ReviewGame(models.Model):
    title = models.CharField(max_length=250, verbose_name="Назавие игры")
    slug = models.SlugField(unique='publish', verbose_name='Слаг')
    author = models.ForeignKey(User, on_delete = models.CASCADE,
                               related_name='blog_post')
    body = models.TextField(verbose_name="Текст ревью")
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, upload_to="game_images/", blank=True, verbose_name="Картинка")
    tags = TaggableManager(verbose_name="Тег", help_text="Вводить теги через ',' ")

    class Meta:
        ordering =('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail_review', kwargs={'slug': self.slug})


class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_comment')
    body = models.TextField(verbose_name="Комментарий")
    publish = models.DateTimeField(default=timezone.now)








# Create your models here.
