from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travel/$', views.index, name='travel'),
    url(r'^travel/add$', views.travel_form),
    url(r'^travel/post/(?P<user_id>\d+)$', views.travel_post),
    url(r'^travel/(?P<travel_id>\d+)$', views.travel_show),
    url(r'^users/(?P<user_id>\d+)$', views.user_show),
    url(r'^travel/delete/(?P<travel_id>\d+)$', views.delete_travel),
    url(r'^travel/join/(?P<travel_id>\d+)/(?P<user_id>\d+)$', views.join_travel),
    url(r'^travel/unjoin/(?P<travel_id>\d+)/(?P<user_id>\d+)$', views.unjoin_travel)
]