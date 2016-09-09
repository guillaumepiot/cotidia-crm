from django.conf.urls import url

from crm.views.admin.contact import (
    ContactList,
    ContactCreate,
    ContactDetail,
    ContactUpdate,
    ContactDelete
)

urlpatterns = [
    url(r'^$', ContactList.as_view(), name='contact-list'),
    url(r'^add/$', ContactCreate.as_view(), name='contact-add'),
    url(r'^(?P<pk>[\d]+)/$', ContactDetail.as_view(), name='contact-detail'),
    url(
        r'^(?P<pk>[\d]+)/update/$',
        ContactUpdate.as_view(),
        name='contact-update'),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        ContactDelete.as_view(),
        name='contact-delete'),
]
