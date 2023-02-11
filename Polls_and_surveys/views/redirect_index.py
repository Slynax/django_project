from django.shortcuts import redirect
from django.views import View


class RedirectIndexView(View):

    def post(self, request, *args, **kwargs):
        return redirect('index')
