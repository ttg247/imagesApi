from django.urls import re_path
from app import views
 
urlpatterns = [ 
    re_path(r'^app/$', views.picture_list),
    re_path(r'^app/(?P<pk>[0-9]+)$', views.pictures_detail),
]