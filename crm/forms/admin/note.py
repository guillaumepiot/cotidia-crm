from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from crm.models import Note
from account.widgets import SelectDateTimeWidget

###############
# NOTE FORMS #
###############

CHOICES_TUPLE = (
    ('1', 'One'),
    ('2', 'Two')
)

class NoteAddForm(forms.ModelForm):
    
    comment = forms.CharField(
        label='', 
        max_length=3000, 
        widget=forms.HiddenInput(attrs={'class':'form__text'}),
        required=False,
        help_text=_('Maximum 3000 characters.')
        )
        
    class Meta:
        model = Note
        fields = ['comment']

class NoteUpdateForm(NoteAddForm):
    class Meta:
        model = Note
        fields = ['comment']
