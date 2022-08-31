from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LeadsListView(generic.ListView):
    template_name = 'leads/leads_list.html'
