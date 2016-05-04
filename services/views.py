# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from services.models import Service, ServiceType
from django.template import RequestContext
from django.contrib import auth
from django.http import Http404


def services(request, *args, **kwargs):
    context = RequestContext(request, {
        'user': auth.get_user(request),
        'service_types': ServiceType.objects.all(),
        'services': Service.objects.all(),
    })
    return render_to_response('index.html', context)


def service(request, service_id=1, *args, **kwargs):
    try:
        context = RequestContext(request, {
            'services': Service.objects.all(),
            'service': Service.objects.get(id=service_id),
            'service_types': ServiceType.objects.all(),
            'user': auth.get_user(request),
        })
    except Service.DoesNotExist:
        raise Http404("Service does not exist")
    return render_to_response('services/service.html', context)
