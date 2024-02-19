from django.shortcuts import render,redirect
from django.contrib.auth.models import User
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


def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        print(last_name)
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')


  
    
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username

        )
        user.set_password(password)
        user.save()    
   

        

    return render(request, "register.html")