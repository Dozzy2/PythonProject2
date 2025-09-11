from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
        list_display = ('title', 'user', 'completed', 'priority', 'due_date') # Поля для отображения в списке
        list_filter = ('user', 'completed', 'priority', 'due_date') # Фильтры справа
        search_fields = ('title', 'description') # Поиск по этим полям
        ordering = ('completed', '-priority', 'due_date') # Сортировка по умолчанию