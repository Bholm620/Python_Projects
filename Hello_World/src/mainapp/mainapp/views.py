from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    products = ["Cherry", "Ull", "Oraiste", "Su Talon", "Pears", "Wassermelon"]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)