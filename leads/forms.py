from django import forms
from .models import Lead


class LeadModelForm(forms.ModelForm):
    ''' creates a new lead '''
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'description',
            'phone_number',
            'email',
        )
