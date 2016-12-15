from django import forms

from cotidia.crm.models import Company


class CompanyAddForm(forms.ModelForm):

    name = forms.CharField(
        label='',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form__text'})
        )

    class Meta:
        model = Company
        exclude = []


class CompanyUpdateForm(CompanyAddForm):
    class Meta:
        model = Company
        exclude = []
