from django.contrib import admin

from Polls_and_surveys.models.categorie import Categorie
from Polls_and_surveys.models.myquestion import MyQuestion
from Polls_and_surveys.models.myquiz import MyQuiz
from Polls_and_surveys.models.myuser import MyUser
from Polls_and_surveys.models.question import Question
from Polls_and_surveys.models.score import Score
from Polls_and_surveys.models.sub_categorie import Sub_Categorie

admin.site.register(Categorie)
admin.site.register(Sub_Categorie)
admin.site.register(Question)
admin.site.register(Score)
admin.site.register(MyQuiz)
admin.site.register(MyQuestion)
admin.site.register(MyUser)
