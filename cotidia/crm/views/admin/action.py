from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.shortcuts import get_object_or_404

from cotidia.account.utils import StaffPermissionRequiredMixin
from cotidia.crm.models import Action, Contact
from cotidia.crm.forms.admin.action import (
    ActionAddForm,
    ActionUpdateForm)


class ActionList(StaffPermissionRequiredMixin, ListView):
    model = Action
    template_name = 'admin/crm/action/action_list.html'
    permission_required = 'crm.change_action'

    def get_queryset(self):
        return Action.objects.filter()


class ActionDetail(StaffPermissionRequiredMixin, DetailView):
    model = Action
    template_name = 'admin/crm/action/action_detail.html'
    permission_required = 'crm.change_action'


class ActionCreate(StaffPermissionRequiredMixin, CreateView):
    model = Action
    form_class = ActionAddForm
    template_name = 'admin/crm/action/action_form.html'
    permission_required = 'crm.add_action'

    def get(self, request, *args, **kwargs):
        self.object = None
        if request.GET.get('contact'):
            get_object_or_404(
                Contact, id=self.request.GET.get('contact'))
        return super(ActionCreate, self).get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, _('Action has been created.'))
        if self.request.GET.get('contact'):
            return reverse(
                'crm-admin:contact-detail',
                kwargs={'pk': self.request.GET.get('contact')})
        else:
            return reverse(
                'crm-admin:action-detail',
                kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(ActionCreate, self).get_context_data(**kwargs)
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

        return super(ActionCreate, self).form_valid(form)


class ActionUpdate(StaffPermissionRequiredMixin, UpdateView):
    model = Action
    form_class = ActionUpdateForm
    template_name = 'admin/crm/action/action_form.html'
    permission_required = 'crm.change_action'

    def get_success_url(self):
        messages.success(self.request, _('Action details have been updated.'))
        if self.object.contact:
            return reverse(
                'crm-admin:contact-detail',
                kwargs={'pk': self.object.contact.id})
        else:
            return reverse(
                'crm-admin:action-detail',
                kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(ActionUpdate, self).get_context_data(**kwargs)
        context['contact'] = self.object.contact

        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(ActionUpdate, self).get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
            kwargs.update({'contact': self.object.contact})
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.modified_by = self.request.user

        return super(ActionUpdate, self).form_valid(form)


class ActionDelete(StaffPermissionRequiredMixin, DeleteView):
    model = Action
    permission_required = 'crm.delete_action'
    template_name = 'admin/crm/action/action_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Action has been deleted.'))
        return reverse('crm-admin:action-list')
