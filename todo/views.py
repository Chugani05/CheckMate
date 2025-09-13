from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.db.models import F
from django.db.models.functions import Coalesce

from .models import Task

from .forms import AddPostForm


def task_list(request: HttpRequest) -> HttpResponse:
    title = "No tasks added yet"
    tasks = Task.objects.all()
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))


def task_detail(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/task-detail.html', dict(task=task))


def done_task(request: HttpRequest) -> HttpResponse:
    title = "You don't have any completed tasks"
    tasks = Task.objects.filter(done=True)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))


def pending_task(request: HttpRequest) -> HttpResponse:
    title = "At the moment you don't have any pending tasks"
    tasks = Task.objects.filter(done=False)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))


def add_task(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.title)
            task.save()
            return redirect('todo:task-list')
    else:
        form = AddPostForm()
    return render(request, 'tasks/task/add-task.html', dict(form=form))


def edit_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := AddPostForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.title)
            task.save()
            return redirect('todo:task-list')
    else:
        form = AddPostForm(instance=task)
    return render(request, 'tasks/task/edit-task.html', dict(form=form, task=task))


def delete_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.delete()
    return render(request, 'tasks/task/delete-task.html', dict(task=task))


def toggle_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.done = not task.done
    task.save()
    return redirect('todo:task-list')