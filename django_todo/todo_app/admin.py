from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'completed')
    search_fields = ['title', 'description']
    list_filter = ('completed',)

admin.site.register(Todo, TodoAdmin)