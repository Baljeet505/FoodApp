from django.shortcuts import redirect, render
from FoodApp.forms import RecipeForm
# from django.http import HttpResponse
from .models import Recipe
# Create your views here.
def home(request):
    list = Recipe.objects.all()
    context = {'list':list}
    return render(request,'food/index.html',context)

def detail(request,recipe_id):
    recipe = Recipe.objects.get(pk = recipe_id)
    context = {'recipe':recipe}
    return render(request,'food/detail.html',context ) 

def Add_Recipe(request):
    form = RecipeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('FoodApp:home')
    
    return render(request, 'food/Add_Recipe.html',{'form':form})

def update_Recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('FoodApp:home')
    
    return render(request,'food/recipe-form.html',{'form':form,'recipe':recipe})

def Delete_Recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('FoodApp:home')
    
    return render(request, 'food/Delete_Recipe.html',{'recipe':recipe} )