from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Task


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
