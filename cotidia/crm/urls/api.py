from django.conf.urls import url

from cotidia.crm.views import api

urlpatterns = [
    url(r'^enquiry/send/$', api.EnquirySend.as_view(), name='enquiry-send'),
]