from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from .forms import TaskForm
from .models import Task


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Аккаунт {username} создан!')
            return redirect(reverse('login'))  # Убрано пространство имен accounts:
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', context={'form': form})


def task_list(request):
    completed_tasks = Task.objects.filter(completed=True)
    not_completed_tasks = Task.objects.filter(completed=False)

    context = {
        'completed_tasks': completed_tasks,
        'not_completed_tasks': not_completed_tasks,
    }
    return render(request, template_name='todoapp/task_list.html', context=context)


def task_create(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Перенаправьте на страницу входа, если пользователь не вошел в систему

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'todoapp/task_create.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    context = {'task': task}
    return render(request, 'todoapp/task_delete.html', context)


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.completed = not task.completed  #
    task.save()

    return redirect('task_list')


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'task': task}
    return render(request, 'todoapp/task_update.html', context)