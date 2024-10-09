from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Task


def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, 'todo/home.html', dict(tasks=tasks))


def task_detail(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.get(slug=task_slug)
    return render(request, 'todo/tasks/detail.html', dict(task=task))
