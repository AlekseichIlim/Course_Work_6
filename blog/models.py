from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    # slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    picture = models.ImageField(upload_to='catalog/blog/picture', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    owner = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('title', 'content')
        permissions = [
            ('can_edit_published', 'Can edit is_published'),
        ]
