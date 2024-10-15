from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('tasks/<task_slug>', views.task_detail, name='task-detail'),
    path('add-task', views.add_task, name='add-task')
]
