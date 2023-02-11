from django.urls import reverse
from django.views import generic

from Polls_and_surveys.forms.create_question import CreateQuestionForm


class CreateQuestionView(generic.FormView):
    template_name = 'create_question.html'
    form_class = CreateQuestionForm

    def form_valid(self, form):
        quiz_name = form.cleaned_data['quiz']
        question = form.cleaned_data['question']
        picture = form.cleaned_data['picture']
        answer = form.cleaned_data['answer']
        explication = form.cleaned_data['explication']
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('create_question')
