from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),   
    url(r'^register$', views.register),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^shirts/create$', views.create),
    url(r'^events/(?P<id>\d+)$', views.event_show),



]
