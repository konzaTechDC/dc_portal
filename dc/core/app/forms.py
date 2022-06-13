from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactUs

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'phone',
            'message'
        )
        labels ={
            'name': _('Name'),
            'email':_('Email'),
            'phone':_('Phone'),
            'message':_('Message'),
        }
        localized_fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'message': SummernoteWidget(),
        }

        error_messages = {
            'message': {
                'max_length': _("This comment is too long."),
            },
        }