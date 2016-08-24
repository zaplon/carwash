# encoding: utf-8
from crispy_forms.layout import Layout, Field, Submit
from django.forms import ModelForm
from django.forms.fields import DateField
from .models import Invoice
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from django.conf import settings
import datetime


class FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        self.template = 'formset.html'
        self.form_tag = False
        self.layout = Layout('service', 'quantity', 'unit', 'price', 'vat')


class CreateForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['nr', 'contractor', 'due_date']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'nr', 'contractor', 'total',
            # FormActions(
            #     Submit(u'Utwórz', u'Utwórz', css_class="btn-success"),
            #     Submit(u'Anuluj', u'Anuluj', css_class="btn-danger"),
            # )
        )
        today = datetime.datetime.today()
        invoice_count = Invoice.objects.filter(date__month=today.strftime('%M')).count() + 1
        self.fields['nr'].initial = '%s%s' % (today.strftime(settings.INVOICE_NR_FORMAT), invoice_count)