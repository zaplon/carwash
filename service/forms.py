# encoding: utf-8
from crispy_forms.layout import Layout, Field, Submit, HTML
from django.forms import ModelForm, Form
from django.forms.fields import DateField
from extra_views import InlineFormSet

from bill.models import ServiceToBill
from invoice.models import ServiceToInvoice
from .models import Service
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from django.conf import settings
import datetime


FORM_FIELDS = ['name', 'code', 'price', 'vat']


class CreateForm(ModelForm):
    class Meta:
        model = Service
        fields = FORM_FIELDS

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            'name', 'code', 'price', 'vat',
            FormActions(
                HTML(u'<a class="btn btn-danger" href="/uslugi/" role="button">Anuluj</a>'),
                Submit(u'Utwórz', u'Utwórz', css_class="btn-success"),
            )
        )


class UpdateForm(CreateForm):

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            'name', 'code', 'price', 'vat',
            FormActions(
                HTML(u'<a class="btn btn-danger" href="/uslugi/" role="button">Anuluj</a>'),
                Submit(u'Zapisz', u'Zapisz', css_class="btn-success"),
            )
        )


class ServiceInlineForm(ModelForm):
    fields = ['service', 'quantity', 'vat', 'price']

    def __init__(self, *args, **kwargs):
        super(ServiceInlineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.template = 'formset.html'
        try:
            self.number = int(self.prefix.split('-')[-1])
        except:
            self.number = "__prefix__"
        self.fields['vat'].widget.attrs['disabled'] = True

