from django.conf.urls import url
from . import views  # . means current dir

app_name = 'notes'

urlpatterns = [
    # /notes
    url(r'^$', views.IndexView, name='index'),  # default section

    # /notes/123
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView, name="detail"),

    # /notes/123/continue
    url(r'^(?P<pk>[0-9]+)/continue$',
        views.conitnue_notes, name="notes-add-continue"),

    # /notes/add
    url(r'^add/$', views.create_notes, name="notes-add"),

    # -------------for random things-------------------
    # /notes/random
    url(r'^random/$', views.create_random_notes, name="notes-random-add"),

    # /notes/random_id/random_update
    url(r'^(?P<pk>[0-9]+)/random_update/$',
        views.modify_random_notes.as_view(), name='notes-random-modify'),

    # /notes/random_display
    url(r'^random_display/$', views.RandomView, name="random_detail"),

    # /notes/note_id/update_notes
    url(r'^(?P<pk>[0-9]+)/modify_notes/$',
        views.modify_notes.as_view(), name='notes-modify'),

    # /notes/python
    url(r'^(?P<note_type>[a-zA-Z. -]+)/$', views.NotesView, name="notes-view"),

    # /notes/python/page_num
    url(r'^(?P<note_type>[a-zA-Z. -]+)/(?P<page_num>[0-9]+)/$',
        views.NotesView, name="notes-notes-list"),

    # /notes/python/sub_category
    url(r'^(?P<note_type>[a-zA-Z. -]+)/(?P<sub_category>[a-zA-Z. -]+)/$',
        views.NotesView, name="notes-sub-view"),

    # /notes/python/sub_category/page_num
    url(r'^(?P<note_type>[a-zA-Z. -]+)/(?P<sub_category>[a-zA-Z. -]+)/(?P<page_num>[0-9]+)/$',
        views.NotesView, name="notes-sub-notes-list"),

    # /notes/python/sub_category/tc
    url(r'^(?P<note_type>[a-zA-Z. -]+)/(?P<sub_category>[a-zA-Z. -]+)/tc$',
        views.NotesSubTC, name="notes-sub-tc"),

    # /notes/python/sub_category/group_name
    url(r'^(?P<note_type>[a-zA-Z. -]+)/(?P<sub_category>[a-zA-Z. -]+)/(?P<info_group>[a-zA-Z. -]+)$',
        views.NotesView, name="notes-sub-group")


]
