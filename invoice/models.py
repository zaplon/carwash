# encoding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.forms.widgets import TextInput

from contractor.models import Contractor
from service.models import Service


class ServiceM2M(models.Model):
    service = models.ForeignKey(Service, verbose_name=u'Usługa')
    quantity = models.IntegerField(default=1, verbose_name=u'Ilość')
    name = models.CharField(max_length=100, verbose_name=u'Nazwa')
    discount = models.FloatField(verbose_name=u'Zniżka', blank=True, null=True)
    price = models.FloatField(verbose_name=u'Cena jednostkowa brutto')
    vat = models.IntegerField()


class ServiceToInvoice(ServiceM2M):
    invoice = models.ForeignKey('Invoice')


class Invoice(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'Data')
    payed = models.BooleanField(default=False, verbose_name=u'Zapłacono')
    total = models.FloatField(default=0, verbose_name=u'W sumie')
    services = models.ManyToManyField(Service, through=ServiceToInvoice, related_name='invoices', verbose_name=u'Usługi')
    due_date = models.DateField(verbose_name=u'Termin płatności')
    nr = models.CharField(max_length=20, verbose_name=u'Nr faktury')
    contractor = models.ForeignKey(Contractor, related_name='invoices', verbose_name=u'Nabywca')

    def __unicode__(self):
        return self.nr

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'pk': self.pk})