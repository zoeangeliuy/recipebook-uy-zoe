from django.urls import path, include
from .views import RecipesListView, RecipesDetailView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name='recipeslist'),
    path('recipe/<int:pk>', RecipesDetailView.as_view(), name='recipe'),
    path('accounts/', include('django.contrib.auth.urls'))
]

app_name = "ledger"
