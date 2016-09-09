from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from account.utils import StaffPermissionRequiredMixin
from crm.models import Company
from crm.forms.admin.company import (
    CompanyAddForm,
    CompanyUpdateForm)


class CompanyList(StaffPermissionRequiredMixin, ListView):
    model = Company
    template_name = 'admin/crm/company/company_list.html'
    permission_required = 'crm.change_company'

    def get_queryset(self):
        return Company.objects.filter()


class CompanyDetail(StaffPermissionRequiredMixin, DetailView):
    model = Company
    template_name = 'admin/crm/company/company_detail.html'
    permission_required = 'crm.change_company'


class CompanyCreate(StaffPermissionRequiredMixin, CreateView):
    model = Company
    form_class = CompanyAddForm
    template_name = 'admin/crm/company/company_form.html'
    permission_required = 'crm.add_company'

    def get_success_url(self):
        messages.success(self.request, 'Company has been created.')
        return reverse(
            'crm-admin:company-detail',
            kwargs={'pk': self.object.id})


class CompanyUpdate(StaffPermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyUpdateForm
    template_name = 'admin/crm/company/company_form.html'
    permission_required = 'crm.change_company'

    def get_success_url(self):
        messages.success(self.request, 'Company details have been updated.')
        return reverse(
            'crm-admin:company-detail',
            kwargs={'pk': self.object.id})


class CompanyDelete(StaffPermissionRequiredMixin, DeleteView):
    model = Company
    permission_required = 'crm.delete_company'
    template_name = 'admin/crm/company/company_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Company has been deleted.'))
        return reverse('crm-admin:company-list')
