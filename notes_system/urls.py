"""notes_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views # . means current dir

#handler404 = 'notes_system.views.view404'
#handler403 = 'notes_system.views.view404'
#handler500 = 'notes_system.views.view404'
#handler400 = 'notes_system.views.view404'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notes/', include('notes.urls')),
    url(r'^food/', include('food.urls')),
    url(r'^redir/', include('redir.urls')),
    url(r'^$', views.IndexView, name = 'index'),
    url(r'^about_me/$', views.AboutView, name = 'about')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
