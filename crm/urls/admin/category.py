from django.conf.urls import url, patterns

from crm.views.admin.category import *

urlpatterns = patterns(
    '',
    # Category management
    url(r'^$', CategoryList.as_view(), name='category-list'),
    url(r'^add/$', CategoryCreate.as_view(), name='category-add'),
    url(r'^(?P<pk>[\d]+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^(?P<pk>[\d]+)/update/$', CategoryUpdate.as_view(), name='category-update'),
    url(r'^(?P<pk>[\d]+)/delete/$', CategoryDelete.as_view(), name='category-delete'),
)

# Include in your main project urls.py
# url(r'^admin/model/', include('app.urls.admin', namespace="model-admin")),
# If you create public urls
# url(r'^model/', include('app.urls.public', namespace="model-public")),
