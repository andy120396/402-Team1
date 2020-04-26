from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def subpage(request):
    return render(request, 'subpage.html')
