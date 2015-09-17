from django.conf.urls import url

from semantic import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uri>[-\w]+)/$', views.resource, name='detail'),
]
