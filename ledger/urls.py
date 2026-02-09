from django.contrib import admin
from django.urls import path
from .views import recipeslist

urlpatterns = [
    path('recipes/list',recipeslist, name='recipes-list')
]

app_name = "ledger"