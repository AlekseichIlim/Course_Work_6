from urllib import request

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import DispatchForm, ClientForm, MessageForm
from mailing.models import Dispatch, Client, Attempts, Message
from mailing.services import send_mailing


class DispatchListView(ListView):
    """Список рассылок"""

    model = Dispatch

    def get_context_data(self, **kwargs):
        context = super(DispatchListView, self).get_context_data(**kwargs)
        mailings = Dispatch.objects.filter(status='завершена')
        context['dispatch_completed'] = mailings
        return context


class DispatchCreateView(CreateView, LoginRequiredMixin):
    """Создание новой рассылки"""

    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy('mailing:dispatch_list')

    def form_valid(self, form):
        """Присваивание владельца при создании рассылки"""

        dispatch = form.save()
        user = self.request.user
        dispatch.owner = user
        dispatch.save()
        return super().form_valid(form)


class DispatchDetailView(DetailView):
    """Просмотр рассылки"""

    model = Dispatch

    def get_context_data(self, **kwargs):
        context = super(DispatchDetailView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(dispatch=self.object)
        return context


class DispatchUpdateView(UpdateView, LoginRequiredMixin):
    """Изменение рассылки"""

    model = Dispatch
    form_class = DispatchForm

    def get_success_url(self):
        return reverse('mailing:dispatch_list')

        # return reverse('mailing:dispatch_list', args=[self.kwargs.get('pk')])


class DispatchDeleteView(DeleteView, LoginRequiredMixin):
    """Удаление рассылки"""

    model = Dispatch
    success_url = reverse_lazy('mailing:dispatch_list')


class AttemptsListView(ListView):
    """Отчет проведенных рассылок"""

    model = Attempts


class ClientListView(ListView):
    """Список клиентов"""

    model = Client

    def get_context_data(self, *args, **kwargs):
        """Выводит пользователю список клиентов, создателем которых он является"""

        context_data = super().get_context_data(*args, **kwargs)
        # products = get_product_from_cache()
        clients = Client.objects.filter(owner=self.request.user)
        context_data['object_list'] = clients
        return context_data


class ClientDetailView(DetailView):
    """Просмотр клиента"""

    model = Client


class ClientUpdateView(UpdateView, LoginRequiredMixin):
    """Изменение клиента"""

    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailing:client_list')


class ClientCreateView(CreateView, LoginRequiredMixin):
    """Создание нового клиента"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        """Присваивание владельца при создании клиента """

        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientDeleteView(DeleteView, LoginRequiredMixin):
    """Удаление клиента"""

    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    """Список сообщений"""

    model = Message

    def get_context_data(self, *args, **kwargs):
        """Выводит пользователю список сообщений, создателем которых он является"""

        context_data = super().get_context_data(*args, **kwargs)
        # products = get_product_from_cache()
        messages = Message.objects.filter(owner=self.request.user)
        context_data['object_list'] = messages
        return context_data


class MessageCreateView(CreateView, LoginRequiredMixin):
    """Создание нового сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        """Присваивание владельца при создании сообщения"""

        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class MessageDetailView(DetailView):
    """Просмотр сообщения"""
    model = Message


class MessageUpdateView(UpdateView, LoginRequiredMixin):
    """Изменение клиента"""

    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse('mailing:message_list')


class MessageDeleteView(DeleteView, LoginRequiredMixin):
    """Удаление клиента"""

    model = Message
    success_url = reverse_lazy('mailing:message_list')