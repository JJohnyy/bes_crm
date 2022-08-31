from django.urls import path
from .views import LeadsListView


urlpatterns = [
    path('', LeadsListView.as_view(), name="leads"),
]
