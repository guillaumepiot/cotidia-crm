from django.conf.urls import url, patterns, include

urlpatterns = [
    url(r'^contact/', include('crm.urls.admin.contact')),
    url(r'^company/', include('crm.urls.admin.company')),
    url(r'^category/', include('crm.urls.admin.category')),
]