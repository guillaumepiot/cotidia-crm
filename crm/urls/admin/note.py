from django.conf.urls import url, patterns

from crm.views.admin.note import *

urlpatterns = patterns(
    '',
    # Note management
    # url(r'^$', NoteList.as_view(), name='note-list'),
    url(r'^add/$', NoteCreate.as_view(), name='note-add'),
    # url(r'^(?P<pk>[\d]+)/$', NoteDetail.as_view(), name='note-detail'),
    url(r'^(?P<pk>[\d]+)/update/$', NoteUpdate.as_view(), name='note-update'),
    url(r'^(?P<pk>[\d]+)/delete/$', NoteDelete.as_view(), name='note-delete'),
)

# Include in your main project urls.py
# url(r'^admin/model/', include('app.urls.admin', namespace="model-admin")),
# If you create public urls
# url(r'^model/', include('app.urls.public', namespace="model-public")),
