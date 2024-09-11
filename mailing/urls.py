from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import DispatchListView, DispatchCreateView, DispatchDetailView, DispatchUpdateView, DispatchDeleteView, AttemptsListView

app_name = MailingConfig.name

urlpatterns = [
    path('', DispatchListView.as_view(), name='dispatch_list'),
    path('dispatch/attempts/', AttemptsListView.as_view(), name='attempts_list'),
    path('dispatch/create/', DispatchCreateView.as_view(), name='dispatch_create'),
    path('dispatch/<int:pk>/', DispatchDetailView.as_view(), name='dispatch_detail'),
    path('dispatch/edit/<int:pk>/', DispatchUpdateView.as_view(), name='dispatch_update'),
    path('dispatch/delete/<int:pk>/', DispatchDeleteView.as_view(), name='dispatch_delete'),

]