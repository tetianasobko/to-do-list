from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Task, Tag


class Index(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags").order_by(
        "is_completed", "-created_at"
    )
    template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:index")


def toggle_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("tasks:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tag_list"
