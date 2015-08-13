from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uri>00)/$', views.scheme, name='scheme'),
    url(r'^(?P<uri>T?[0-9a-zA-Z]+)/$', views.resource, name='detail'),
]