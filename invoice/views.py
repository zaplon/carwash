from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Invoice
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet
from .models import ServiceToInvoice


class ServicesInline(InlineFormSet):
    model = ServiceToInvoice
    fields = ['service', 'quantity', 'price']
    max_num = 20
    extra = 3
    can_delete = True


class InvoiceListView(ListView):

    model = Invoice

    def get_context_data(self, **kwargs):
        context = super(InvoiceListView, self).get_context_data(**kwargs)
        return context


class InvoiceDetailView(DetailView):

    model = Invoice

    def get_context_data(self, **kwargs):
        context = super(InvoiceDetailView, self).get_context_data(**kwargs)
        return context


class InvoiceCreate(CreateWithInlinesView):
    model = Invoice
    form_class = CreateForm
    inlines = [ServicesInline]

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreate, self).get_context_data(**kwargs)
        context['formset_helper'] = FormSetHelper()
        return context


class InvoiceUpdate(UpdateView):
    model = Invoice
    fields = ['date']