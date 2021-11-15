from django.shortcuts import render
from .models import Place


def home(request):

    obj1 = Place.objects.all()
    params = {'obj': obj1}

    return render(request, 'index.html', params)
