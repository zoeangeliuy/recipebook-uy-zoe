from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe


class RecipesListView(ListView):
    model=Recipe
    template_name= "recipeslist.html"

class RecipesDetailView(DetailView):
    model=Recipe
    template_name= "recipe.html"

