# Generated by Django 4.0.4 on 2022-05-15 06:11

import ckeditor.fields
import core.models.about
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_infopagemodel_body_en_infopagemodel_body_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificatesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=core.models.about.upload_location)),
            ],
        ),
    ]
