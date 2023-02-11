from django.db import models


class MyQuiz(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default='')
    picture = models.ImageField(null=True, default=None, upload_to='media/img/')
    create_by = models.ForeignKey('MyUser', on_delete=models.CASCADE, null=True, blank=True, default=None,
                                  related_name='user_quiz')

    def __str__(self):
        return self.name