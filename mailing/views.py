from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from mailing.forms import DispatchForm
from mailing.models import Dispatch


class DispatchListView(ListView):
    model = Dispatch


class DispatchCreateView(CreateView):
    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy('mailing:dispatch_list')
