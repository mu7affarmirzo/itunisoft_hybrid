from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'about/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class AboutInfoModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class CertificatesModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.img.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.title)


class VacancyModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Vacancies'
        verbose_name_plural = 'Vacancies'
