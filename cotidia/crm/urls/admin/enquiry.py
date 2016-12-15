from django.conf.urls import url

from cotidia.crm.views.admin.enquiry import (
    EnquiryList,
    EnquiryDetail,
    EnquiryDelete
)

urlpatterns = [
    # Enquiry management
    url(r'^$', EnquiryList.as_view(), name='enquiry-list'),
    url(r'^(?P<pk>[\d]+)/$', EnquiryDetail.as_view(), name='enquiry-detail'),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        EnquiryDelete.as_view(),
        name='enquiry-delete'),
]
