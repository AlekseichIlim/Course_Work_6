from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import DispatchForm
from mailing.models import Dispatch, Client


class DispatchListView(ListView):
    model = Dispatch


class DispatchCreateView(CreateView):
    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy('mailing:dispatch_list')


class DispatchDetailView(DetailView):
    model = Dispatch

    def get_context_data(self, **kwargs):
        context = super(DispatchDetailView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(dispatch=self.object)
        print(context['clients'])
        return context


class DispatchUpdateView(UpdateView):
    model = Dispatch
    form_class = DispatchForm

    def get_success_url(self):
        return reverse('mailing:dispatch_detail', args=[self.kwargs.get('pk')])


class DispatchDeleteView(DeleteView):
    model = Dispatch
    success_url = reverse_lazy('mailing:dispatch_list')
