from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['completed_date', 'due_date'], 'classes': ['collapse']})
    ]

admin.site.register(Todo, TodoAdmin)
