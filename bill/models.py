# encoding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.forms.widgets import TextInput

from contractor.models import Contractor
from invoice.models import ServiceM2M
from service.models import Service


class ServiceToBill(ServiceM2M):
    bill = models.ForeignKey('Bill')


class Bill(models.Model):
    service = models.ManyToManyField(Service, through=ServiceToBill, related_name='bills', verbose_name=u'Usługi')
    nr = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('bill-detail', kwargs={'pk': self.pk})
