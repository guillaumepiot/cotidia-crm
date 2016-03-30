import json
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages 
from django.conf import settings
from django.shortcuts import get_object_or_404

from account.utils import StaffPermissionRequiredMixin
from crm.models import Enquiry


######################
# Enquiry management #
######################

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
