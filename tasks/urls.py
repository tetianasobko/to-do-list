from django.urls import path, include

urlpatterns = [
    path("", Index.as_view(), name="index"),
]

appname = "tasks"