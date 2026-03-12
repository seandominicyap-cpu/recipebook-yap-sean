from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage

# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]
    search_fields = ('name',)
    list_display = ('name',)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
