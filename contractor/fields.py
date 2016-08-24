# encoding: utf-8
from django.forms.fields import CharField
from django.forms import ValidationError
import re

NIP_RE = re.compile(
    r'[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}')
NIP_RE_2 = re.compile(
    r'[0-9]{3}[0-9]{3}[0-9]{2}[0-9]{2}')


def validate_nip(value):
    if not NIP_RE.match(value) and not NIP_RE_2.match(value):
        raise ValidationError(u"NIP musi mieć postać XXX-XXX-XX-XX")


class Nip(CharField):

    def __init__(self, *args, **kwargs):
        kwargs.update({
            'min_length': 10,
            'max_length': 13,
            'validators': kwargs.get('validators', [validate_nip])
        })
        super(Nip, self).__init__(*args, **kwargs)