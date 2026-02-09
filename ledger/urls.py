from django.contrib import admin
from django.urls import path
from .views import recipeslist, recipe1,recipe2

urlpatterns = [
    path('recipes/list',recipeslist, name='recipes-list'),
    path('recipe/1',recipe1, name='recipe1'),
    path('recipe/2',recipe2, name='recipe2')
]

app_name = "ledger"