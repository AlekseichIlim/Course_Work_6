from urllib import request

from django.conf import settings
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import DispatchForm
from mailing.models import Dispatch, Client, Attempts
from mailing.services import send_mailing


class DispatchListView(ListView):
    model = Dispatch

    def get_context_data(self, **kwargs):
        context = super(DispatchListView, self).get_context_data(**kwargs)
        mailings = Dispatch.objects.filter(status='завершена')
        context['dispatch_completed'] = mailings
        return context


class DispatchCreateView(CreateView):
    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy('mailing:dispatch_list')



class DispatchDetailView(DetailView):
    model = Dispatch

    def get_context_data(self, **kwargs):
        context = super(DispatchDetailView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(dispatch=self.object)
        return context


class DispatchUpdateView(UpdateView):
    model = Dispatch
    form_class = DispatchForm


    def get_success_url(self):
        return reverse('mailing:dispatch_detail', args=[self.kwargs.get('pk')])


class DispatchDeleteView(DeleteView):
    model = Dispatch
    success_url = reverse_lazy('mailing:dispatch_list')


class AttemptsListView(ListView):
    model = Attempts
