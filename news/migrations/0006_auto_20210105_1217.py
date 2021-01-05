# Generated by Django 3.1.4 on 2021-01-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201228_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', through='news.PostCategory', to='news.Category', verbose_name='Тэг'),
        ),
    ]
