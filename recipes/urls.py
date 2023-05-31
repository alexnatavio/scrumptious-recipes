from django.urls import path, include
from django.contrib import admin
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe, my_recipe_list

urlpatterns = [
    path('recipes/', recipe_list, name="recipe_list"),
    path('recipes/<int:id>', show_recipe, name="show_recipe"),
    path('recipes/create', create_recipe, name="create_recipe"),
    path('recipes/<int:id>/edit/', edit_recipe, name="edit_recipe"),
    path('mine/', my_recipe_list, name="my_recipe_list"),


]
