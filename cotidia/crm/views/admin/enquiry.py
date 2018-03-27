# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import DeleteView
# from django.urls import reverse
# from django.utils.translation import ugettext_lazy as _
# from django.contrib import messages

# from cotidia.account.utils import StaffPermissionRequiredMixin
# from cotidia.crm.models import Enquiry


# class EnquiryList(StaffPermissionRequiredMixin, ListView):
#     model = Enquiry
#     template_name = 'admin/crm/enquiry/enquiry_list.html'
#     permission_required = 'crm.change_enquiry'

#     def get_queryset(self):
#         return Enquiry.objects.filter()


# class EnquiryDetail(StaffPermissionRequiredMixin, DetailView):
#     model = Enquiry
#     template_name = 'admin/crm/enquiry/enquiry_detail.html'
#     permission_required = 'crm.change_enquiry'


# class EnquiryDelete(StaffPermissionRequiredMixin, DeleteView):
#     model = Enquiry
#     permission_required = 'crm.delete_enquiry'
#     template_name = 'admin/crm/enquiry/enquiry_confirm_delete.html'

#     def get_success_url(self):
#         messages.success(self.request, _('Enquiry has been deleted.'))
#         return reverse('crm-admin:enquiry-list')


from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminDeleteView
)

from cotidia.crm.models import Enquiry


class EnquiryList(AdminListView):
    columns = (
        ('Type', 'enquiry_type'),
        ('Email', 'email'),
        ('Date', 'date_created'),
    )
    model = Enquiry
    add_view = False
    row_actions = ['view']
    row_click_action = 'detail'


class EnquiryDetail(AdminDetailView):
    model = Enquiry
    fieldsets = [
        {
            "legend": "Enquiry details",
            "fields": [
                [
                    {
                        "label": "Data",
                        "field": "data",
                    }
                ]
            ]
        }
    ]


class EnquiryDelete(AdminDeleteView):
    model = Enquiry

