from django.conf.urls import url, include

urlpatterns = [
    url(r'^contact/note/', include('cotidia.crm.urls.admin.note')),
    url(r'^contact/', include('cotidia.crm.urls.admin.contact')),
    url(r'^company/', include('cotidia.crm.urls.admin.company')),
    url(r'^category/', include('cotidia.crm.urls.admin.category')),
    url(r'^action/', include('cotidia.crm.urls.admin.action')),
    url(r'^enquiry/', include('cotidia.crm.urls.admin.enquiry')),
]
