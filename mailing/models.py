from datetime import datetime
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Клиент"""

    email = models.EmailField(verbose_name='почта', unique=True)
    name = models.CharField(max_length=150, verbose_name='имя')
    surname = models.CharField(max_length=150, verbose_name='фамилия')
    comments = models.TextField(verbose_name='коментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.surname}, почта:{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('name', 'surname')


class Message(models.Model):
    """Сообщение рассылки"""

    topic_message = models.CharField(max_length=100, verbose_name='тема сообщения')
    title_message = models.CharField(max_length=100, verbose_name='заголовок')
    body_message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return self.title_message

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('title_message', 'topic_message')


class Dispatch(models.Model):
    """Рассылка"""

    DAILY = 'раз в день'
    WEEKLY = 'раз в неделю'
    MONTHLY = 'раз в месяц'

    CREATED = 'создана'
    LAUNCHED = 'запущена'
    CANCELLED = 'отменена'
    COMPLETED = 'завершена'
    DELETED = 'удалена'

    PERIODICITY_CHOICES = [
        (DAILY, 'раз в день'),
        (WEEKLY, 'раз в неделю'),
        (MONTHLY, 'раз в месяц')
    ]

    STATUS_CHOICES = [
        (CREATED, 'создана'),
        (LAUNCHED, 'запущена'),
        (CANCELLED, 'отменена'),
        (COMPLETED, 'завершена'),
    ]

    title = models.CharField(max_length=100, verbose_name='заголовок', **NULLABLE)
    first_sent_date_time = models.DateTimeField(verbose_name='дата и время первой отправки')
    next_sent_date_time = models.DateTimeField(default=None, verbose_name='дата и время следующей отправки', **NULLABLE, editable=False,)
    last_sent_date_time = models.DateTimeField(default=None, verbose_name='дата и время последней отправки')
    periodicity = models.CharField(max_length=20, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    status = models.CharField(default=CREATED, max_length=20, choices=STATUS_CHOICES, verbose_name='статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', related_name='dispatch')
    clients = models.ManyToManyField(Client, verbose_name='клиенты', related_name='dispatch')
    owner = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('title', 'first_sent_date_time', 'status',)


class Attempts(models.Model):
    """Попытка рассылки"""

    datetime = models.DateTimeField(verbose_name='дата и время последней отправки')
    status = models.BooleanField(default=True, verbose_name='успешно')
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE, verbose_name='рассылка', related_name='attempts')
    mail_response = models.CharField(max_length=100, verbose_name='ответ почтового сервиса', **NULLABLE)

    def __str__(self):
        return f'Отправка {self.dispatch} : {self.datetime}'

    class Meta:
        verbose_name = 'Попытка отправки'
        verbose_name_plural = 'Попытки отправки'
        ordering = ('datetime', 'status', 'dispatch',)
