from django.shortcuts import reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    
    def get_success_url(self):
        return reverse("login")


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    form_class = UserChangeForm
    template_name = "members/profile_edit.html"

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile_edit")


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "members/dashboard.html"
    success_url = reverse_lazy('dashboard')
