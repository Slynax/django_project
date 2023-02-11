from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class MyUser(User):

    def login(self, request, username, password):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False

    def logout(self, request):
        logout(request)

    def __str__(self):
        return self.username