from django.conf.urls import url
from . import views # . means current dir
from .models import Notes

app_name = 'notes'

urlpatterns = [
    # /notes
    url(r'^$', views.IndexView, name = 'index'), # default section
    
    # /notes/python
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView, name = "detail"),

    # /notes/add
    url(r'add/$', views.create_notes, name = "notes-add"),

    # /notes/note_id/delete_notes
    url(r'^(?P<notes_id>[0-9]+)/delete_notes/$', views.delete_notes, name='notes-delete'),

    # /notes/note_id/update_notes
    url(r'^(?P<pk>[0-9]+)/modify_notes/$', views.modify_notes.as_view(), name='notes-modify'),

    # /notes/python
    url(r'^(?P<note_type>[a-zA-Z ]+)/$', views.NotesView, name = "notes-view"),

    # /notes/python/sub_category
    url(r'^(?P<note_type>[a-zA-Z ]+)/(?P<sub_category>[a-zA-Z ]+)/$', views.NotesSubView, name = "notes-sub-view"),

    # /notes/python/sub_category/tc
    url(r'^(?P<note_type>[a-zA-Z ]+)/(?P<sub_category>[a-zA-Z ]+)/tc$', views.NotesSubTC, name = "notes-sub-tc"),

    # /notes/python/sub_category/group_name
    url(r'^(?P<note_type>[a-zA-Z ]+)/(?P<sub_category>[a-zA-Z ]+)/(?P<info_group>[a-zA-Z ]+)$', views.NotesSubGroup, name = "notes-sub-group"),

]
    

