# Generated by Django 2.1.2 on 2018-12-19 14:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0007_auto_20181217_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='article_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
