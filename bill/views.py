from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Bill
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from extra_views import InlineFormSet, CreateWithInlinesView
from .models import ServiceToBill


class BillListView(ListView):

    model = Bill

    def get_context_data(self, **kwargs):
        context = super(BillListView, self).get_context_data(**kwargs)
        return context


class ServicesInline(InlineFormSet):
    model = ServiceToBill
    fields = ['service', 'quantity', 'vat', 'price']
    max_num = 20
    extra = 3
    can_delete = True

    def __init__(self, *args, **kwargs):
        super(ServicesInline, self).__init__(*args, **kwargs)
        pass


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


class BillUpdate(UpdateView):
    model = Bill
    fields = ['date']