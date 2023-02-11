from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default='')
    picture = models.ImageField(null=True, default=None, upload_to='media/img/')

    def __str__(self):
        return self.name
