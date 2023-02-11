from django.views.generic import ListView

from Polls_and_surveys.models.categorie import Categorie


class IndexView(ListView):
    template_name = 'index.html'
    model = Categorie