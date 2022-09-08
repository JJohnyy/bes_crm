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

    def __init__(self, *args, **kwargs):
        """ remove labels, add placeholders """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'description': 'Description',
            'phone_number': 'Phone Number',
            'email': 'Email',
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].label = ''
            self.fields[field].widget.attrs['placeholder'] = placeholder
