# Generated by Django 4.0.4 on 2022-05-15 06:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_aboutinfomodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopagemodel',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='infopagemodel',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='infopagemodel',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='infopagemodel',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='infopagemodel',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infopagemodel',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infopagemodel',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infopagemodel',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
