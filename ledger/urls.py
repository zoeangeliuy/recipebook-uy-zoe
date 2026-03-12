from django.urls import path
from .views import RecipesListView, RecipesDetailView, RecipesCreateView, RecipesCreateImageView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name='recipeslist'),
    path('recipe/add', RecipesCreateView.as_view(), name='add_recipe'),
    path('recipe/<int:pk>', RecipesDetailView.as_view(), name='recipe'),
    path('recipe/<int:pk>/add_image', RecipesCreateImageView.as_view(), name='add_recipe_image')
]

app_name = "ledger"
