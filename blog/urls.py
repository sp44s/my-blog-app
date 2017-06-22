

from django.conf.urls import url
from . import views

urlpatterns = [
        url( r'^$', views.post_list, name='thiscanbeanything'),
        url( r'^post/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
]