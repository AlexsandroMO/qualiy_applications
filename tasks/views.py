from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm

from .models import Task

import data_upgrate

def hello(request):
    return HttpResponse('hello!')

def index(request):
    tasks = Task.objects.all().order_by('inspection_name')
    return render(request, 'tasks/index.html', {'tasks': tasks})


def entryvalue(request, name):
    tasks = Task.objects.all().order_by('inspection_name')
    return render(request, 'tasks/entryvalue.html', {'name':name, 'tasks': tasks})


def entryvalue(request, name):
    return render(request, 'tasks/entryvalue.html', {'name':name})


def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task':task})


def newtask(request):
    if request.method == 'POST':
        form = TaskForm()

        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/add-task.html', {'form':form})

