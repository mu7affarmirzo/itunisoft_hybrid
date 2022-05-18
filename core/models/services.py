from django.db import models
from core.models.home import upload_location


class ServicesModel(models.Model):
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

    class Meta:
        verbose_name = 'Bizning xizmatlar'
        verbose_name_plural = 'Bizning xizmatlar'


class ProjectFormModel(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name = 'Qoldirilgan arizalar'
        verbose_name_plural = 'Qoldirilgan arizalar'
