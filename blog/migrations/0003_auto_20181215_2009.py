# Generated by Django 2.1.2 on 2018-12-15 12:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181215_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]