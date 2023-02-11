from django import forms

from Polls_and_surveys.models.myquiz import MyQuiz


class CreateQuizForm(forms.ModelForm):
    picture = forms.ImageField(label='Image', required=True)

    class Meta:
        model = MyQuiz
        fields = ['name', 'picture']
        labels = {
            'name': 'Nom',
            'picture': 'Image',
        }
