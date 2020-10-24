from django.shortcuts import render
from django.http import HttpResponse

from . models import Task

import data_upgrate

def hello(request):
    return HttpResponse('hello!')

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def entryvalue(request, name):
    data_upgrate.read_sql_update
    #print(teste)
    tasks = Task.objects.all()
    return render(request, 'tasks/entryvalue.html', {'name':name, 'tasks': tasks})
