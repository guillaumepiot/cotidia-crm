from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from crm.models import Category
from account.widgets import SelectDateTimeWidget

##################
# CATEGORY FORMS #
##################

class CategoryAddForm(forms.ModelForm):
    
    name = forms.CharField(
        label='', 
        max_length=255, 
        widget=forms.TextInput(attrs={'class':'form__text'})
        )
        
    class Meta:
        model = Category
        exclude = []

class CategoryUpdateForm(CategoryAddForm):
    class Meta:
        model = Category
        exclude = []
