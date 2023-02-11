from django import forms

from Polls_and_surveys.models.myquestion import MyQuestion
from Polls_and_surveys.models.myquiz import MyQuiz


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = MyQuestion
        fields = ['question', 'picture', 'answer', 'explication', 'quiz']
        labels = {
            'question': 'Question',
            'picture': 'Image',
            'answer': 'Réponse',
            'explication': 'Explication',
            'quiz': 'Nom du quiz',
        }
        answer = forms.BooleanField(widget=forms.CheckboxInput)
        explication = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['quiz'].queryset = MyQuiz.objects.filter(create_by=user)
