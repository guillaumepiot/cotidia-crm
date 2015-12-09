import json
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages 
from django.conf import settings

from account.utils import StaffPermissionRequiredMixin
from crm.models import Contact
from crm.forms.admin.contact import (
    ContactAddForm,
    ContactUpdateForm)


####################
# Contact management #
####################

class ContactList(StaffPermissionRequiredMixin, ListView):
    model = Contact
    template_name = 'admin/crm/contact/contact_list.html'
    permission_required = 'crm.change_contact'
    paginate_by = 25

    def get_queryset(self):
        #
        # Get filter params
        #
        first_letter = self.request.GET.get('first_letter')

        query = Contact.objects.filter()

        if first_letter:
            query = query.filter(first_name__startswith=first_letter)

        return query

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContactList, self).get_context_data(**kwargs)
        # Get the filter params
        first_letter = self.request.GET.get('first_letter')
        if first_letter:
            context['first_letter'] = first_letter
        return context

class ContactDetail(StaffPermissionRequiredMixin, DetailView):
    model = Contact
    template_name = 'admin/crm/contact/contact_detail.html'
    permission_required = 'crm.change_contact'

class ContactCreate(StaffPermissionRequiredMixin, CreateView):
    model = Contact
    form_class = ContactAddForm
    template_name = 'admin/crm/contact/contact_form.html'
    permission_required = 'crm.add_contact'

    def get_success_url(self):
        messages.success(self.request, _('Contact has been created.'))
        return reverse('crm-admin:contact-detail', kwargs={'pk':self.object.id})

class ContactUpdate(StaffPermissionRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactUpdateForm
    template_name = 'admin/crm/contact/contact_form.html'
    permission_required = 'crm.change_contact'

    def get_success_url(self):
        messages.success(self.request, _('Contact details have been updated.'))
        return reverse('crm-admin:contact-detail', kwargs={'pk':self.object.id})

class ContactDelete(StaffPermissionRequiredMixin, DeleteView):
    model = Contact
    permission_required = 'crm.delete_contact'
    template_name = 'admin/crm/contact/contact_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Contact has been deleted.'))
        return reverse('crm-admin:contact-list')
