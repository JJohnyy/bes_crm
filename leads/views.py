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
    context_object_name = 'leads'
  
    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(
            agent=user,
            agent__isnull=False
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadsListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/create_lead.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads')

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.agent = self.request.user
        lead.save()

        messages.success(self.request, "You have successfully created a lead")
        return super(LeadCreateView, self).form_valid(form)
