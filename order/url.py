from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.order_create, name="order_create"),
    url(r'^pay/$', views.pay, name="pay"),
    url(r'^success/$', views.order_success, name="order_success"),
]
