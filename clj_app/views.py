from django.shortcuts import render
from .models import Category
import json

def list_categories(request):
    categories = Category.objects.all()
    print(categories)
    data = {"categories" : categories}
    return render(request, 'clj_app/list_categories.html', data)