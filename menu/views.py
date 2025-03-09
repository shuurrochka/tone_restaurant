from django.shortcuts import render
from .models import Dish

def menu_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/menu_list.html', {'dishes': dishes})