from django.urls import reverse
from django.views import generic

from Polls_and_surveys.forms.create_quiz import CreateQuizForm
from Polls_and_surveys.models.myquiz import MyQuiz
from Polls_and_surveys.models.myuser import MyUser


class CreateQuizView(generic.FormView):
    template_name = 'create_quiz.html'
    form_class = CreateQuizForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        picture = form.cleaned_data['picture']

        user = MyUser.objects.get(username=self.request.user.username)
        MyQuiz.objects.create(name=name, picture=picture, create_by=user)
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse('create_question')


