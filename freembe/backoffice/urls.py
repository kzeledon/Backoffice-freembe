from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^inicio$', views.index, name='index'),
     url(r'^backoffice$', views.backoffice, name='index'),
    ]
