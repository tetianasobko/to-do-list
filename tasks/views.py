from django.shortcuts import render
from django.views import generic

from tasks.models import Task


class Index(generic.ListView):
    model = Task
    template_name = "tasks/index.html"

