from django.shortcuts import render
from .models import Recipe

# Create your views here.


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }

    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id) }

    return render(request, 'recipe_detail.html', ctx)



