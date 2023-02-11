from django.contrib import messages
from django.urls import reverse
from django.views import generic

from Polls_and_surveys.forms.register import RegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from Polls_and_surveys.models.myuser import MyUser


class RegisterFormView(generic.FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            MyUser.objects.create_user(
                username=username, email=email, password=password
            )
            messages.add_message(
                self.request, messages.INFO, 'User created successfully'
            )
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid login credentials')


        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
