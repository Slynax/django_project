from django.views.generic import ListView

from Polls_and_surveys.models.myquiz import MyQuiz


class MyQuizView(ListView):
    template_name = 'my_quiz.html'
    model = MyQuiz

    def get_queryset(self):
        user = self.request.user
        quiz = list(MyQuiz.objects.filter(create_by=user))
        return quiz