from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uri>00)/$', views.scheme, name='scheme'),
    url(r'^(?P<uri>[0-9]{2})/$', views.collection, name='collection'),
    url(r'^(?P<uri>[0-9]{6})/$', views.collection, name='collection'),
    url(r'^(?P<uri>T?[0-9a-zA-Z]+)/$', views.resource, name='detail'),
]
