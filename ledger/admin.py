
from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    search_fields = ('name', )
    list_display = ('name',)
    inlines = [RecipeIngredientInline,]

class ProfileAdmin(admin.ModelAdmin):
    model = Profile

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile, ProfileAdmin)
