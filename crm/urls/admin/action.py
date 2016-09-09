from django.conf.urls import url

from crm.views.admin.action import (
    ActionList,
    ActionCreate,
    ActionDetail,
    ActionUpdate,
    ActionDelete
)

urlpatterns = [
    url(r'^$', ActionList.as_view(), name='action-list'),
    url(r'^add/$', ActionCreate.as_view(), name='action-add'),
    url(r'^(?P<pk>[\d]+)/$', ActionDetail.as_view(), name='action-detail'),
    url(
        r'^(?P<pk>[\d]+)/update/$',
        ActionUpdate.as_view(),
        name='action-update'),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        ActionDelete.as_view(),
        name='action-delete'),
]
