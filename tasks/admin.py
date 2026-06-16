from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'owner', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
