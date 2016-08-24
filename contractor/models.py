from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from contractor.fields import validate_nip
from django.db import models


class Contractor(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Nazwa')
    address = models.CharField(max_length=200, verbose_name=u'Adres')
    city = models.CharField(max_length=200, verbose_name=u'Miasto')
    zipcode = models.CharField(max_length=6, verbose_name=u'Kod pocztowy')
    nip = models.CharField(max_length=13, verbose_name=u'NIP', validators=[validate_nip])

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.nip)

    def get_absolute_url(self):
        #return reverse('contractor-detail', kwargs={'pk': self.pk})
        return reverse('contractor-list')