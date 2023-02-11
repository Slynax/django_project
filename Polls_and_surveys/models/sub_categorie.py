from django.db import models

from Polls_and_surveys.models.categorie import Categorie


class Sub_Categorie(models.Model):
    category_fk = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='category_pk')
    name = models.CharField(max_length=200, null=True, blank=True, default='')
    picture = models.ImageField(null=True, default=None, upload_to='media/img/')

    def __str__(self):
        return self.name