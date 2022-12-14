from django.urls import path
from .views import (
    LeadsListView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView
    )


urlpatterns = [
    path('', LeadsListView.as_view(), name="leads"),
    path('create/', LeadCreateView.as_view(), name="leads_create"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="leads_update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="leads_delete"),
]
