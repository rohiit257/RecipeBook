from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def recipes(request):

    if request.method == "POST":

        data = request.POST
        print(data)

        recipe_name = data.get('recipe_name')
        recipe_desc= data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')

        recipe.objects.create(
            recipe_name= recipe_name,
            recipe_desc= recipe_desc,
            recipe_img= recipe_img

        )
    queryset = recipe.objects.all()
    
    search = request.GET.get('search')

    if search:
        queryset = queryset.filter(recipe_name__icontains = search)

    data = {
        'recipe':queryset
    }

    return render(request , "recipes.html" , data)


def delete_recipe(request , id):
    queryset = recipe.objects.get(id = id)
    queryset.delete()
    return redirect('recipes')


def update_recipe(request, id):
    queryset = recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_desc= data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc

        if recipe_img:
            queryset.recipe_img= recipe_img
        
        queryset.save()
        print(queryset)
        return redirect('recipes')


    data = {
        'recipe': queryset
    }


    return render(request , "update_recipe.html" , data)