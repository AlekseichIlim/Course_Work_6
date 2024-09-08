from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from mailing.forms import DispatchForm
from mailing.models import Dispatch


class DispatchListView(ListView):
    model = Dispatch


class DispatchCreateView(CreateView):
    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy('mailing:dispatch_list')


class DispatchDetailView(DetailView):
    model = Dispatch


class DispatchUpdateView(UpdateView):
    model = Dispatch
    form_class = DispatchForm

    def get_success_url(self):
        return reverse('mailing:dispatch_detail', args=[self.kwargs.get('pk')])