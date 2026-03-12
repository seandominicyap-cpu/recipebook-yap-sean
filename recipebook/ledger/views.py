from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe, RecipeImage
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }

    return render(request, 'recipe_list.html', ctx)


@login_required
def recipe_detail(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)
           }

    return render(request, 'recipe_detail.html', ctx)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('ledger:recipe_list')


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = 'recipe_image_form.html'

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'id': self.kwargs['pk']})
