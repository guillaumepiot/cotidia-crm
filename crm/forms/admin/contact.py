from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from crm.models import Contact, Company, Category
from crm import settings as crm_settings 
from account.widgets import SelectDateTimeWidget

###############
# CONTACT FORMS #
###############

class ContactAddForm(forms.ModelForm):
    
    title = forms.ChoiceField(
        label="",
        choices=crm_settings.TITLE,
        widget=forms.Select(attrs={'class':'form__select'})
        )

    first_name = forms.CharField(
        label='', 
        max_length=50, 
        widget=forms.TextInput(
            attrs={'class':'form__text', 'placeholder': _('First name')})
        )

    last_name = forms.CharField(
        label='', 
        max_length=50, 
        widget=forms.TextInput(
            attrs={'class':'form__text', 'placeholder': _('Last name')})
        )
        
    company = forms.ModelChoiceField(
        label="",
        queryset=Company.objects.all(),
        widget=forms.Select(attrs={'class':'form__select'}),
        required=False
        )
        
    category = forms.ModelMultipleChoiceField(
        label='',
        widget=forms.CheckboxSelectMultiple,
        queryset=Category.objects.all(),
        required=False
        )
        
    class Meta:
        model = Contact
        exclude = []

class ContactUpdateForm(ContactAddForm):
    class Meta:
        model = Contact
        exclude = []
