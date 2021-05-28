# Generated by Django 3.2.3 on 2021-05-26 17:47

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0003_auto_20210524_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewgame',
            name='body',
            field=models.TextField(verbose_name='Текст ревью'),
        ),
        migrations.AlterField(
            model_name='reviewgame',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='game_images/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='reviewgame',
            name='slug',
            field=models.SlugField(unique='publish', verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='reviewgame',
            name='tags',
            field=taggit.managers.TaggableManager(help_text="Вводить теги через ',' ", through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='reviewgame',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Назавие игры'),
        ),
    ]
