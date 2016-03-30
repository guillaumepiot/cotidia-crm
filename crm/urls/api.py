from django.conf.urls import patterns, include, url

from crm.views import api

urlpatterns = [
	url(r'^enquiry/send/$', api.EnquirySend.as_view(), name='enquiry-send'),
]