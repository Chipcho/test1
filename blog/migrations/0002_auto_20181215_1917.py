# Generated by Django 2.1.2 on 2018-12-15 11:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]