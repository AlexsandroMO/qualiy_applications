from django.shortcuts import render
from django.http import HttpResponse

from . models import Task

def hello(request):
    return HttpResponse('hello!')


def index(request):
    tasks = Task.objects.all()
    
    return render(request, 'tasks/index.html', {'tasks': tasks})

def entryvalue(request, name):

    return render(request, 'tasks/entryvalue.html', {'name':name})

