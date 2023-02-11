from django.db import models

from Polls_and_surveys.models.sub_categorie import Sub_Categorie


class Question(models.Model):
    question = models.CharField(max_length=200, null=True, blank=True, default='')
    sub_category_fk = models.ForeignKey(Sub_Categorie, on_delete=models.CASCADE, null=True, blank=True,
                                        related_name='sub_category_pk')
    picture = models.ImageField(null=True, default=None, upload_to='media/img/')
    answer = models.BooleanField(default=False)
    explication = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return self.question