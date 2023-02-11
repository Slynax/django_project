import random

from django.views.generic import ListView

from Polls_and_surveys.models.myuser import MyUser
from Polls_and_surveys.models.question import Question
from Polls_and_surveys.models.score import Score
from Polls_and_surveys.models.sub_categorie import Sub_Categorie


class QuizView(ListView):
    template_name = 'quiz.html'
    model = Sub_Categorie

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        questions = list(Question.objects.filter(sub_category_fk=pk))
        random.shuffle(questions)

        return questions
        # autre solution
        # return Question.objects.filter(sub_category_fk=pk).order_by('?')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = MyUser.objects.get(username=self.request.user)
            score, created = Score.objects.get_or_create(user=user)
            context['score'] = score.score
        context['csrf_token'] = self.request.META['CSRF_COOKIE']
        return context

