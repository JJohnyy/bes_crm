from django.urls import path
from .views import LeadsListView, LeadCreateView, LeadUpdateView


urlpatterns = [
    path('', LeadsListView.as_view(), name="leads"),
    path('create/', LeadCreateView.as_view(), name="leads_create"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="leads_update"),
]
