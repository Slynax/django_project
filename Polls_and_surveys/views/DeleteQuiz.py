from django.shortcuts import redirect
from django.views import View

from Polls_and_surveys.models.myquiz import MyQuiz


class DeleteQuizView(View):

    def delete_quiz(self, pk):
        quiz = MyQuiz.objects.get(id=pk)
        quiz.delete()
        return redirect('my_quiz')

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        return self.delete_quiz(pk)


