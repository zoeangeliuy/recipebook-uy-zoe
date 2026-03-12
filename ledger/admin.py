
from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )
    list_display = ('name',)
    inlines = [RecipeIngredientInline, RecipeImageInline]


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile, ProfileAdmin)
