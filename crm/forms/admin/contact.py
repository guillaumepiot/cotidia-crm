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

    email = forms.EmailField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(
            attrs={'class':'form__text'}),
        required=False
        )

    phone_number = forms.CharField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(
            attrs={'class':'form__text'}),
        required=False
        )

    mobile_number = forms.CharField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(
            attrs={'class':'form__text'}),
        required=False
        )

    website = forms.URLField(
        label='', 
        max_length=150, 
        widget=forms.TextInput(
            attrs={'class':'form__text'}),
        required=False
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

    #
    # Address
    #
    first_line = forms.CharField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder':_("First line"), 'class':'form__text'}),
        required=False
        )

    second_line = forms.CharField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder':_("Second line"), 'class':'form__text'}),
        required=False
        )

    county = forms.CharField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder':_("County / State"), 'class':'form__text'}),
        required=False
        )

    city = forms.CharField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder':_("City"), 'class':'form__text'}),
        required=False
        )

    postcode = forms.CharField(
        label='', 
        max_length=50, 
        widget=forms.TextInput(attrs={'placeholder':_("Postcode"), 'class':'form__text'}),
        required=False
        )

    country = forms.ChoiceField(
        label="",
        choices=crm_settings.COUNTRIES,
        widget=forms.Select(attrs={'class':'form__select'}),
        required=False
        )

    lat = forms.DecimalField(
        label='', 
        widget=forms.HiddenInput(attrs={'placeholder':_("Latitude"), 'class':'form__text'}),
        required=False
        )

    lng = forms.DecimalField(
        label='', 
        widget=forms.HiddenInput(attrs={'placeholder':_("Longitude"), 'class':'form__text'}),
        required=False
        )
        
    class Meta:
        model = Contact
        exclude = []

class ContactUpdateForm(ContactAddForm):
    class Meta:
        model = Contact
        exclude = []
