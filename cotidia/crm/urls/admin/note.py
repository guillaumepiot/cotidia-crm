from django.conf.urls import url

from cotidia.crm.views.admin.note import (
    NoteCreate,
    NoteUpdate,
    NoteDelete
)

urlpatterns = [
    url(r'^add/$', NoteCreate.as_view(), name='note-add'),
    url(r'^(?P<pk>[\d]+)/update/$', NoteUpdate.as_view(), name='note-update'),
    url(r'^(?P<pk>[\d]+)/delete/$', NoteDelete.as_view(), name='note-delete'),
]
