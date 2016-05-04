# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20160421_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'db_table': 'service_type',
                'verbose_name': '\u0422\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438',
            },
        ),
        migrations.AlterField(
            model_name='service',
            name='created_date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceType', verbose_name='\u0422\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438'),
        ),
    ]