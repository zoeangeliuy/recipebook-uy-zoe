from django.contrib import admin
from django.urls import path
from .views import RecipesListView

urlpatterns = [
    path('recipes/list',RecipesListView.as_view(), name='recipeslist')
]

app_name = "ledger"