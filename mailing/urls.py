from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import DispatchListView, DispatchCreateView, DispatchDetailView, DispatchUpdateView, \
    DispatchDeleteView, AttemptsListView, ClientListView, MessageListView, ClientDetailView, ClientUpdateView, \
    ClientCreateView, ClientDeleteView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', DispatchListView.as_view(), name='dispatch_list'),
    path('dispatch/attempts/', AttemptsListView.as_view(), name='attempts_list'),
    path('dispatch/create/', DispatchCreateView.as_view(), name='dispatch_create'),
    path('dispatch/<int:pk>/', DispatchDetailView.as_view(), name='dispatch_detail'),
    path('dispatch/edit/<int:pk>/', DispatchUpdateView.as_view(), name='dispatch_update'),
    path('dispatch/delete/<int:pk>/', DispatchDeleteView.as_view(), name='dispatch_delete'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
]
