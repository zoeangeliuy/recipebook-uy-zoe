from django.http import HttpResponse
from django.shortcuts import render

from .forms import RecipeForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Profile

class RecipesCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipeform.html"
    success_url = "/recipes/list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = Profile.objects.all()
        context["form"]= RecipeForm()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class RecipesListView(ListView):
    model = Recipe
    template_name = "recipeslist.html"


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    redirect_field_name = '/accounts/login'
