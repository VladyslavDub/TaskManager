from django.shortcuts import render
from .models import *


def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'base.html', context)


def category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)

