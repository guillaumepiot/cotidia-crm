from django import forms

from cotidia.crm.models import Contact, Action
from cotidia.account.widgets import SelectDateWidget, SelectTimeWidget


class ActionAddForm(forms.ModelForm):

    title = forms.CharField(
        label='',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form__text'})
        )

    description = forms.CharField(
        label='',
        max_length=3000,
        widget=forms.Textarea(attrs={'class': 'form__text'}),
        required=False
        )

    due_date = forms.DateField(
        label="",
        widget=SelectDateWidget(attrs={'class': "form__select"})
        )

    due_time = forms.TimeField(
        label="",
        widget=SelectTimeWidget(attrs={'class': "form__select"}),
        required=False
        )

    contact = forms.ModelChoiceField(
        label="",
        queryset=Contact.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form__select'}),
        required=False
        )

    completed = forms.BooleanField(
        required=False, label="Completed")

    class Meta:
        model = Action
        exclude = []

    def __init__(self, contact=None, *args, **kwargs):
        super(ActionAddForm, self).__init__(*args, **kwargs)

        if contact:
            del self.fields['contact']


class ActionUpdateForm(ActionAddForm):
    class Meta:
        model = Action
        exclude = []
