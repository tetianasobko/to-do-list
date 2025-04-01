from django.views import generic

from tasks.models import Task


class Index(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags").order_by("is_completed", "-created_at")
    template_name = "tasks/index.html"

