from django.conf.urls import url

from semantic import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uri>[0-9a-zA-Z\s]+)/$', views.resource, name='detail'),
]
