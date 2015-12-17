from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from crm.models import Contact, Action
from account.widgets import SelectDateWidget, SelectTimeWidget

###############
# ACTION FORMS #
###############

CHOICES_TUPLE = (
    ('1', 'One'),
    ('2', 'Two')
)

class ActionAddForm(forms.ModelForm):
    
    title = forms.CharField(
        label='', 
        max_length=255, 
        widget=forms.TextInput(attrs={'class':'form__text'})
        )

    description = forms.CharField(
        label='', 
        max_length=3000, 
        widget=forms.Textarea(attrs={'class':'form__text'}),
        required=False
        )

    due_date = forms.DateField(
        label="", 
        widget=SelectDateWidget(required=False, attrs={'class': "form__select"})
        )

    due_time = forms.TimeField(
        label="", 
        widget=SelectTimeWidget(required=False, attrs={'class': "form__select"}),
        required=False
        )
        
    contact = forms.ModelChoiceField(
        label="",
        queryset=Contact.objects.all(),
        widget=forms.Select(attrs={'class':'form__select'}),
        required=False
        )
        
    completed = forms.BooleanField(
        required=False, label=_("Completed"))
        
        
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
