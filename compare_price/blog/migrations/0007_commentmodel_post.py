# Generated by Django 3.2.3 on 2021-05-28 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210526_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='blog.reviewgame'),
            preserve_default=False,
        ),
    ]