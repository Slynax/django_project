from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name", min_length=5, max_length=100, )
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",
                               min_length=5, max_length=100,
                               widget=forms.PasswordInput())

    def clean(self):
        pass

    def clean_username(self):
        if self.cleaned_data['username'] == '':
            self.add_error('username', "username can't be empty!")
        return self.cleaned_data['username']

    def clean_email(self):
        if self.cleaned_data['email'] == '':
            self.add_error('email', "email can't be empty!")
        return self.cleaned_data['email']

    def clean_password(self):
        if self.cleaned_data['password'] == '':
            self.add_error('password', "password can't be empty!")
        return self.cleaned_data['password']