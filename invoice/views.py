from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Invoice
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet
from .models import ServiceToInvoice
from django.db.models import Q


class InvoiceListView(ListView):

    model = Invoice

    def get_context_data(self, **kwargs):
        context = super(InvoiceListView, self).get_context_data(**kwargs)
        if self.request.GET.get('query', False):
            context['query'] = self.request.GET['query']
        return context

    def get_queryset(self):
        query = super(InvoiceListView, self).get_queryset()
        if self.request.GET.get('query', False):
            query = query.filter(Q(contractor__name__icontains=self.request.GET['query']) |
                                 Q(contractor__nip__icontains=self.request.GET['query']))
        return query


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


class InvoiceUpdate(InvoiceCreate):
    pass