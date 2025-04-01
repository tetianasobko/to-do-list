from django.contrib import admin

from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("description", "deadline", "is_completed")
    search_fields = ("description",)
    list_filter = ("is_completed",)
    ordering = ("-deadline",)
    date_hierarchy = "deadline"

admin.site.register(Tag)
