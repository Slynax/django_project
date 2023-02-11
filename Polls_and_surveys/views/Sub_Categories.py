from django.views.generic import DetailView

from Polls_and_surveys.models.categorie import Categorie


class Sub_CategoriesView(DetailView):
    template_name = 'sub_categories.html'
    model = Categorie
