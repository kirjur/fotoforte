# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ServiceType(models.Model):

    class Meta():
        db_table = 'service_type'
        verbose_name = "Тип услуги"

    name = models.CharField(max_length=200, verbose_name="Наименование")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Service(models.Model):

    class Meta():
        db_table = 'service'
        verbose_name = "Услуга"

    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    created_date = models.DateTimeField(verbose_name="Дата создания")
    service_type = models.ForeignKey(
        ServiceType, default=1, verbose_name="Тип услуги")

    def __str__(self):
        return self.name
