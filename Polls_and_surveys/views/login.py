from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from Polls_and_surveys.forms.login import LoginForm



class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid login credentials')
        return render(request, 'login.html', {'form': form})
