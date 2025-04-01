from django.urls import path

from tasks.views import (
    Index,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task
)


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle/", toggle_task, name="task-toggle"
    ),
]

app_name = "tasks"
