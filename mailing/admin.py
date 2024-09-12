from django.contrib import admin

from mailing.models import Client, Message, Dispatch, Attempts
from users.models import User


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname')
    search_fields = ('email', 'surname', 'owner')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title_message', )
    list_filter = ('title_message', 'topic_message')
    search_fields = ('title_message', 'topic_message', 'owner')


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_filter = ('title', 'first_sent_date_time', 'periodicity', 'status')
    search_fields = ('title', 'message', 'first_sent_date_time', 'owner')


@admin.register(Attempts)
class AttemptsAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime', 'dispatch', 'status')
    list_filter = ('dispatch', 'datetime', 'status')
    search_fields = ('dispatch', 'datetime')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('email', )
