from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse


class ReviewGame(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique='publish')
    author = models.ForeignKey(User, on_delete = models.CASCADE,
                               related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, upload_to="game_images/", blank=True)

    class Meta:
        ordering =('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail_review', kwargs={'slug': self.slug})




# Create your models here.
