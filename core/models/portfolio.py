from django.db import models
from core.models.home import upload_location


class PortfolioModel(models.Model):
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    @property
    def imageURL(self):
        try:
            url = str(self.img.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.title)
