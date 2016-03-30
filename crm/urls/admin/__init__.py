from django.conf.urls import url, patterns, include

urlpatterns = [
	url(r'^contact/note/', include('crm.urls.admin.note')),
    url(r'^contact/', include('crm.urls.admin.contact')),
    url(r'^company/', include('crm.urls.admin.company')),
    url(r'^category/', include('crm.urls.admin.category')),
    url(r'^action/', include('crm.urls.admin.action')),
    url(r'^enquiry/', include('crm.urls.admin.enquiry')),
]