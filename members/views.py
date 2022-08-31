from django.shortcuts import reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    
    def get_success_url(self):
        return reverse("login")


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "members/dashboard.html"
    success_url = reverse_lazy('dashboard')
