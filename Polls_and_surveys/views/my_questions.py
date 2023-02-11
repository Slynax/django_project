import random

from django.shortcuts import redirect
from django.views.generic import ListView

from Polls_and_surveys.models.myquestion import MyQuestion
from Polls_and_surveys.models.myquiz import MyQuiz


class MyQuestionsView(ListView):
    template_name = 'my_questions.html'
    model = MyQuiz

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        questions = list(MyQuestion.objects.filter(quiz=pk))
        random.shuffle(questions)
        return questions
