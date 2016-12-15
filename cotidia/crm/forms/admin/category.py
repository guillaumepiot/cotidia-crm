from django import forms

from cotidia.crm.models import Category


class CategoryAddForm(forms.ModelForm):

    name = forms.CharField(
        label='',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form__text'})
        )

    class Meta:
        model = Category
        exclude = []


class CategoryUpdateForm(CategoryAddForm):
    class Meta:
        model = Category
        exclude = []
