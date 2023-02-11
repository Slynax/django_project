from django.db import models


class MyQuestion(models.Model):
    question = models.CharField(max_length=200, null=True, blank=True, default='')
    picture = models.ImageField(null=True, default=None, upload_to='media/img/')
    answer = models.BooleanField(default=False)
    explication = models.TextField(null=True, blank=True, default='')
    quiz = models.ForeignKey('MyQuiz', on_delete=models.CASCADE, null=True, blank=True, default=None,
                             related_name='myquiz')

    def __str__(self):
        return self.question