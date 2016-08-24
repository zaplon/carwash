# encoding: utf-8
from crispy_forms.layout import Layout, Field, Submit
from django.forms import ModelForm
from django.forms.fields import DateField
from .models import Bill
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
        self.layout = Layout('service', 'quantity', 'price')


class CreateForm(ModelForm):
    class Meta:
        model = Bill
        fields = ['nr']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            'nr', 'name',
        )
        today = datetime.datetime.today()
        bill_count = Bill.objects.filter(date__month=today.strftime('%M')).count() + 1
        self.fields['nr'].initial = '%s%s' % (today.strftime(settings.BILL_NR_FORMAT), bill_count)