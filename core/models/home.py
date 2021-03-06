from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import random as r


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'home/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class PartnerCategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Hamkorlar Kategoriyasi'
        verbose_name_plural = 'Hamkorlar Kategoriyasi'


class PartnersModel(models.Model):
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)
    category = models.ForeignKey(PartnerCategoryModel, related_name='partners', on_delete=models.SET_NULL, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.img.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.category.name)

    class Meta:
        verbose_name = 'Hamkorlarimiz'
        verbose_name_plural = 'Hamkorlarimiz'


class CarouselModel(models.Model):
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)
    title = models.TextField()

    @property
    def imageURL(self):
        try:
            url = str(self.img.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.title)




class StatsModel(models.Model):
    numbers = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)


class InfoPageModel(models.Model):
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.title)


@receiver(post_save, sender=InfoPageModel)
def pre_save_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1, 10000)) + "-" + str(r.randint(1, 10000)))
