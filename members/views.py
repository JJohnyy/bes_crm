from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    succes_url = reverse_lazy('login')

class DashboardView(generic.CreateView):
    template_name = "members/dashboard.html"
    success_url = reverse_lazy('dashboard')

