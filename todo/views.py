
from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
from .forms import TaskForm





def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html',context)

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'task': task}
    return render(request, 'todo/edit_task.html', context)

def delete_task(request, id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task':task}
    return render(request, 'todo/delete_task.html',context)

def complete_task(request,id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    return redirect('/')

