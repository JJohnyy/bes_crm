from django.shortcuts import reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.


class CustomUserCreationForm(generic.CreateView):
    '''creates user'''
    form_class = CustomUserCreationForm
    template_name = "registration/registration.html"
    
    def get_success_url(self):
        return reverse("login")


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    ''''updates user data'''
    form_class = UserChangeForm
    template_name = "members/profile_edit.html"

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile_edit")


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    ''' dashboard view '''
    template_name = "members/dashboard.html"
    success_url = reverse_lazy('dashboard')
