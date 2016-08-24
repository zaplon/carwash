from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name=u'Nazwa')
    code = models.CharField(max_length=25, verbose_name=u'Kod')
    price = models.FloatField(verbose_name=u'Cena')
    vat = models.FloatField(default=0, verbose_name=u'Stawka VAT')
    unit = models.CharField(max_length=50, verbose_name=u'Jednostka')

    def __unicode__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        #return reverse('contractor-detail', kwargs={'pk': self.pk})
        return reverse('service-list')
