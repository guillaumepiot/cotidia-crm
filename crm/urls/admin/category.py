from django.conf.urls import url

from crm.views.admin.category import (
    CategoryList,
    CategoryCreate,
    CategoryDetail,
    CategoryUpdate,
    CategoryDelete
)


urlpatterns = [
    url(r'^$', CategoryList.as_view(), name='category-list'),
    url(r'^add/$', CategoryCreate.as_view(), name='category-add'),
    url(r'^(?P<pk>[\d]+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(
        r'^(?P<pk>[\d]+)/update/$',
        CategoryUpdate.as_view(),
        name='category-update'),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        CategoryDelete.as_view(),
        name='category-delete'),
]
