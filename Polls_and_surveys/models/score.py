from django.db import models

from Polls_and_surveys.models.myuser import MyUser


class Score(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='scores')
    score = models.IntegerField(default=0)