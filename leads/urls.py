from django.urls import path
from .views import LeadsListView, LeadCreateView


urlpatterns = [
    path('', LeadsListView.as_view(), name="leads"),
    path('create/', LeadCreateView.as_view(), name="leads_create"),
]
