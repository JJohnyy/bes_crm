from django.shortcuts import render, reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import LeadModelForm
from . models import Lead

# Create your views here.

User = get_user_model()

class LeadsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/leads_list.html'

    queryset = Lead.objects.all()
    get_object_name = 'leads'   


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/create_lead.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads')

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.user = self.request.user
        lead.save()

        messages.success(self.request, "You have successfully created a lead")
        return super(LeadCreateView, self).form_valid(form)

