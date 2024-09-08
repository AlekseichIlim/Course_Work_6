from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import DispatchListView, DispatchCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', DispatchListView.as_view(), name='dispatch_list'),
    path('dispatch/create/', DispatchCreateView.as_view(), name='dispatch_create'),
]