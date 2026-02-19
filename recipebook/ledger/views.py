from django.shortcuts import render
from .models import Recipe

# Create your views here.

RECIPES_CONTEXT = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"}
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2cup"},
                {"name": "water", "quantity": "1 cup"}, # Corrected key from 'quanity'
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"}
            ],
            "link": "/recipe/2"
        }
    ]
}

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }

    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id) }

    return render(request, 'recipe_detail.html', ctx)



#def recipe_1(request):
    # Pass only the first recipe's data
  #  context = RECIPES_CONTEXT["recipes"][0]
   # return render(request, 'ledger/recipe_detail.html', context)

#def recipe_2(request):
    # Pass only the second recipe's data
  #  context = RECIPES_CONTEXT["recipes"][1]
 #   return render(request, 'ledger/recipe_detail.html', context)

