from django.urls import path
from .views import UserRegisterView, DashboardView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('dashoard/', DashboardView.as_view(), name='dashboard'),
]
