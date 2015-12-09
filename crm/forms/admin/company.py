from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from crm.models import Company
from account.widgets import SelectDateTimeWidget

###############
# COMPANY FORMS #
###############

class CompanyAddForm(forms.ModelForm):
    
    name = forms.CharField(
        label='', 
        max_length=255, 
        widget=forms.TextInput(attrs={'class':'form__text'})
        )
        
    class Meta:
        model = Company
        exclude = []

class CompanyUpdateForm(CompanyAddForm):
    class Meta:
        model = Company
        exclude = []
