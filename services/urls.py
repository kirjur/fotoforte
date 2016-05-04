# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.services, name='services'),
    url(r'^(\d+)/$', views.service, name='service'),

]
