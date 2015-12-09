from django.conf.urls import url

from crm.views.admin.company import *

urlpatterns = [
    # Company management
    url(r'^$', CompanyList.as_view(), name='company-list'),
    url(r'^add/$', CompanyCreate.as_view(), name='company-add'),
    url(r'^(?P<pk>[\d]+)/$', CompanyDetail.as_view(), name='company-detail'),
    url(r'^(?P<pk>[\d]+)/update/$', CompanyUpdate.as_view(), name='company-update'),
    url(r'^(?P<pk>[\d]+)/delete/$', CompanyDelete.as_view(), name='company-delete'),
]

# Include in your main project urls.py
# url(r'^admin/model/', include('app.urls.admin', namespace="model-admin")),
# If you create public urls
# url(r'^model/', include('app.urls.public', namespace="model-public")),
