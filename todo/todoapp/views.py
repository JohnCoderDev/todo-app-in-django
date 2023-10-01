from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Task

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'todoapp/index.html'
    context_object_name = 'task_list'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.all()

class DetailTaskView(generic.DetailView):
    model = Task
    template_name = 'todoapp/task_details.html' 
    
def mark_as_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.concluded = not task.concluded
    task.conclusion_date = timezone.now() if task.concluded else None
    task.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
    