from django.urls import path

from tasks.views import Index


urlpatterns = [
    path("", Index.as_view(), name="index"),
]

app_name = "tasks"
