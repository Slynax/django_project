from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label='User Name')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
