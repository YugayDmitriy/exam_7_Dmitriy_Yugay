from django.db import models


class Visitors(models.Model):
    CHOISES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    ]

    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    email = models.EmailField(max_length=30, null=True, blank=True, verbose_name='Электронная почта')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=13, choices=CHOISES, null=True, blank=True, default='Новая',
                              verbose_name='Статус')

    class Meta:
        ordering = ["-created_at"]
