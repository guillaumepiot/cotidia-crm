from django import forms

from crm.models import Note


class NoteAddForm(forms.ModelForm):

    comment = forms.CharField(
        label='',
        max_length=3000,
        widget=forms.HiddenInput(attrs={'class': 'form__text'}),
        required=False,
        help_text="Maximum 3000 characters."
        )

    class Meta:
        model = Note
        fields = ['comment']


class NoteUpdateForm(NoteAddForm):
    class Meta:
        model = Note
        fields = ['comment']
