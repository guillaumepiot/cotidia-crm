from django.conf.urls import url

from crm.views.admin.company import (
    CompanyList,
    CompanyCreate,
    CompanyDetail,
    CompanyUpdate,
    CompanyDelete
)

urlpatterns = [
    url(r'^$', CompanyList.as_view(), name='company-list'),
    url(r'^add/$', CompanyCreate.as_view(), name='company-add'),
    url(r'^(?P<pk>[\d]+)/$', CompanyDetail.as_view(), name='company-detail'),
    url(
        r'^(?P<pk>[\d]+)/update/$',
        CompanyUpdate.as_view(),
        name='company-update'),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        CompanyDelete.as_view(),
        name='company-delete'),
]
