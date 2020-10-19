from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello!')


def index(request):
    return render(request, 'tasks/index.html')

def entryvalue(request, name):
    return render(request, 'tasks/entryvalue.html', {'name':name})

