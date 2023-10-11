from django.shortcuts import render
from .forms import thingform

def home(request):
    form = thingform()
    return render(request, 'home.html', {'thingform': thingform})
