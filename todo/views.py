from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .models import Task

from .forms import AddPostForm


def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, 'todo/home.html', dict(tasks=tasks))


def task_detail(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.get(slug=task_slug)
    return render(request, 'todo/tasks/detail.html', dict(task=task))

def add_task(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.title)
            task.save()
            return redirect('todo:task-list')
    else:
        form = AddPostForm()
    return render(request, 'todo/tasks/add_task.html', dict(form=form))