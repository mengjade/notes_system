from django.conf.urls import url
from . import views # . means current dir
from .models import Food

app_name = 'food'

urlpatterns = [
    # /food
    url(r'^$', views.IndexView, name = 'index'), # default section

    # /food/1
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView, name = "detail"),

    # /food/add
    url(r'add/$', views.create_notes, name = "notes-add"),

    # /food/food_id/update_notes
    url(r'^(?P<pk>[0-9]+)/modify_notes/$', views.modify_notes.as_view(), name='notes-modify'),

    # /food/recipe
    url(r'recipe/$', views.RecipeView, name='notes-recipe'),

    # /food/recipe/ing
    url(r'recipe/ing/$', views.RecipeIngView, name='notes-ing'),

    # /food/recipe/tag/
    url(r'recipe/tag/$', views.RecipeTagView, name='notes-tag'),

    # /food/recipe/search_type/search_value
    url(r'recipe/(?P<search_type>[a-zA-Z_]+)/(?P<search_value>.*)/$', views.RecipeSubView, name='notes-recipe'),

    # /food/what_to_cook
    url(r'whattocook/$', views.WTCView, name='notes-wtc'),

    # /food/sweet/recipe/
    url(r'sweet/me/$', views.SweetView, name='notes-sweet'),

    # /food/update_storage
    url(r'^update_storage/$', views.update_storage_view, name='update_storage_view'),

]


