from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def Input_form(request):
    return render(request,"Input_page/form.html")