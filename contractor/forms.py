# encoding: utf-8
from crispy_forms.layout import Layout, Field, Submit, HTML
from django.forms import ModelForm
from django.forms.fields import DateField
from .models import Contractor
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from django.conf import settings
import datetime

FORM_FIELDS = ['nip', 'name', 'address', 'zipcode', 'city']


class CreateForm(ModelForm):
    class Meta:
        model = Contractor
        fields = FORM_FIELDS

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            'nip', 'name', 'address', 'zipcode', 'city',
            FormActions(
                HTML(u'<a class="btn btn-danger" href="../" role="button">Anuluj</a>'),
                Submit(u'Utwórz', u'Utwórz', css_class="btn-success"),
            )
        )