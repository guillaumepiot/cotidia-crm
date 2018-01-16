from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.shortcuts import get_object_or_404

from cotidia.account.utils import StaffPermissionRequiredMixin
from cotidia.crm.models import Note, Contact
from cotidia.crm.forms.admin.note import (
    NoteAddForm,
    NoteUpdateForm)


class NoteCreate(StaffPermissionRequiredMixin, CreateView):
    model = Note
    form_class = NoteAddForm
    template_name = 'admin/crm/note/note_form.html'
    permission_required = 'crm.add_note'

    def get(self, request, *args, **kwargs):
        self.object = None
        if request.GET.get('contact'):
            get_object_or_404(
                Contact, id=self.request.GET.get('contact'))
        return super(NoteCreate, self).get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, _('Note has been created.'))
        return reverse(
            'crm-admin:contact-detail',
            kwargs={'pk': self.object.contact.id}
            )

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(NoteCreate, self).get_context_data(**kwargs)
        if self.request.GET.get('contact'):
            context['contact'] = get_object_or_404(
                Contact, id=self.request.GET.get('contact'))

        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)

        if self.request.GET.get('contact'):
            self.object.contact = get_object_or_404(
                Contact, id=self.request.GET.get('contact'))
            self.object.created_by = self.request.user
        else:
            raise Exception('A contact reference must be submitted.')

        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(StaffPermissionRequiredMixin, UpdateView):
    model = Note
    form_class = NoteUpdateForm
    template_name = 'admin/crm/note/note_form.html'
    permission_required = 'crm.change_note'

    def get_success_url(self):
        messages.success(self.request, _('Note details have been updated.'))
        return reverse(
            'crm-admin:contact-detail',
            kwargs={'pk': self.object.contact.id}
            )

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(NoteUpdate, self).get_context_data(**kwargs)
        context['contact'] = self.object.contact

        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        if not self.object.contact:
            raise Exception('A contact reference must be submitted.')
        self.object = form.save(commit=False)
        self.object.modified_by = self.request.user

        return super(NoteUpdate, self).form_valid(form)


class NoteDelete(StaffPermissionRequiredMixin, DeleteView):
    model = Note
    permission_required = 'crm.delete_note'
    template_name = 'admin/crm/note/note_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Note has been deleted.'))
        return reverse(
            'crm-admin:contact-detail',
            kwargs={'pk': self.contact_id}
            )

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(NoteDelete, self).get_context_data(**kwargs)
        context['contact'] = self.object.contact

        return context

    def delete(self, request, *args, **kwargs):
        self.contact_id = self.get_object().contact.id
        return super(NoteDelete, self).delete(request, *args, **kwargs)
