from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='homePage'),
    url(r'^profile/$', views.profile, name='userProfile')
]
