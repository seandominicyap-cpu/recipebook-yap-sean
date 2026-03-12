from django.urls import path
from . import views

app_name = "ledger"
urlpatterns = [
    path('', views.recipe_list, name='index'),
    path('recipes/list', views.recipe_list, name='recipe_list'),
    path('recipe/<int:id>', views.recipe_detail, name='recipe_detail'),
    path('recipe/add', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image',
         views.RecipeImageCreateView.as_view(), name='add_image'),

]
