from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from cotidia.account.utils import StaffPermissionRequiredMixin
from cotidia.crm.models import Enquiry


class EnquiryList(StaffPermissionRequiredMixin, ListView):
    model = Enquiry
    template_name = 'admin/crm/enquiry/enquiry_list.html'
    permission_required = 'crm.change_enquiry'

    def get_queryset(self):
        return Enquiry.objects.filter()


class EnquiryDetail(StaffPermissionRequiredMixin, DetailView):
    model = Enquiry
    template_name = 'admin/crm/enquiry/enquiry_detail.html'
    permission_required = 'crm.change_enquiry'


class EnquiryDelete(StaffPermissionRequiredMixin, DeleteView):
    model = Enquiry
    permission_required = 'crm.delete_enquiry'
    template_name = 'admin/crm/enquiry/enquiry_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Enquiry has been deleted.'))
        return reverse('crm-admin:enquiry-list')