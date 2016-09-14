from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import Bill, ServiceToBill
from .forms import *
from extra_views import CreateWithInlinesView, UpdateWithInlinesView


class BillListView(ListView):
    model = Bill

    def get_context_data(self, **kwargs):
        context = super(BillListView, self).get_context_data(**kwargs)
        if self.request.GET.get('query', False):
            context['query'] = self.request.GET['query']
        return context


class BillDetailView(DetailView):
    model = Bill

    def get_context_data(self, **kwargs):
        context = super(BillDetailView, self).get_context_data(**kwargs)
        return context


class BillCreate(CreateWithInlinesView):
    model = Bill
    form_class = CreateForm
    inlines = [ServicesInline]

    def get_context_data(self, **kwargs):
        context = super(BillCreate, self).get_context_data(**kwargs)
        context['formset_helper'] = FormSetHelper()
        return context


class BillUpdate(UpdateWithInlinesView):
    model = Bill
    form_class = CreateForm
    inlines = [ServicesInline]

    def get_context_data(self, **kwargs):
        context = super(BillUpdate, self).get_context_data(**kwargs)
        context['formset_helper'] = FormSetHelper()
        return context
