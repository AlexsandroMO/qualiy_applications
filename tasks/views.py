from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
from .models import Task

def hello(request):
    return HttpResponse('hello!')


def template_list(request):

    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(inspection_name__icontains=search)

    else:
        task_list = Task.objects.all().order_by('inspection_name')
        paginator = Paginator(task_list, 12)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/template-list.html', {'tasks': tasks})


def entryvalue(request, name):
    return render(request, 'tasks/entryvalue.html', {'name':name})


def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task':task})


def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/add-task.html', {'form': form})


def editview(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edit-task.html', {'form': form, 'task': task}) 

    else:
        return render(request, 'tasks/edit-task.html', {'form': form, 'task': task})


def deleteview(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Template Deletado com Sucesso!')

    return redirect('/')

