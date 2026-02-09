from django.contrib import admin
from django.urls import path
from .views import recipeslist, recipe1

urlpatterns = [
    path('recipes/list',recipeslist, name='recipes-list'),
    path('recipe/1',recipe1, name='recipe1'),\
]

app_name = "ledger"