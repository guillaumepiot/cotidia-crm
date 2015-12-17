from django.conf.urls import url, patterns

from crm.views.admin.action import *

urlpatterns = [
    # Action management
    url(r'^$', ActionList.as_view(), name='action-list'),
    url(r'^add/$', ActionCreate.as_view(), name='action-add'),
    url(r'^(?P<pk>[\d]+)/$', ActionDetail.as_view(), name='action-detail'),
    url(r'^(?P<pk>[\d]+)/update/$', ActionUpdate.as_view(), name='action-update'),
    url(r'^(?P<pk>[\d]+)/delete/$', ActionDelete.as_view(), name='action-delete'),
]

# Include in your main project urls.py
# url(r'^admin/model/', include('app.urls.admin', namespace="model-admin")),
# If you create public urls
# url(r'^model/', include('app.urls.public', namespace="model-public")),
