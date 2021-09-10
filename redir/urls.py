from django.conf.urls import url
from . import views # . means current dir

app_name = 'redir'

urlpatterns = [
    # /redir
    url(r'^$', views.IndexView, name = 'index'), # default section

    # /redir/aboutus
    url(r'aboutus/$', views.AboutView, name = "au"),

    # /redir/teaching
    url(r'teaching/$', views.TAView, name = "ta"),

    # /redir/bitcoinpricing
    url(r'bitcoinpricing/$', views.BitView, name = "bit"),
]