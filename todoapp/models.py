from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
        PRIORITY_CHOICES = [
            ('low', 'Низкий'),
            ('medium', 'Средний'),
            ('high', 'Высокий'),
        ]
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
        title = models.CharField(max_length=200)
        description = models.TextField(blank=True, null=True)
        completed = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        priority = models.CharField(
            max_length=10,
            choices=PRIORITY_CHOICES,
            default='medium',
            verbose_name='Приоритет'
        )
        due_date = models.DateField(blank=True, null=True, verbose_name='Срок выполнения')

        def __str__(self):
            return self.title

        class Meta:
            ordering = ['completed', '-priority', 'due_date', '-created_at'] # Сортировка задач


class Notification(models.Model):
        NOTIFICATION_TYPES = (
            ('new_task', 'Новая задача'),
            ('task_update', 'Обновление задачи'),
            ('deadline_reminder', 'Напоминание о дедлайне'),
        )
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
        notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
        message = models.TextField()
        is_read = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.user.username} - {self.notification_type}"
