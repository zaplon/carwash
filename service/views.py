from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from extra_views import CreateWithInlinesView

from invoice.views import ServicesInline
from .models import Service
from django.views.generic.edit import CreateView, UpdateView
from .forms import CreateForm, UpdateForm
from django.shortcuts import HttpResponse
from django.db.models import Q
import json


def service_as_json(request):
    if not request.GET.get('id', False):
        return HttpResponse(status=400)
    else:
        s = Service.objects.get(id=request.GET['id'])
        s = {'price': s.price, 'unit': s.unit, 'vat': s.vat}
        return HttpResponse(json.dumps(s), status=200,
                            content_type='application/json')


class ServiceListView(ListView):

    model = Service
    paginate_by = 10

    def get_queryset(self):
        query = super(ServiceListView, self).get_queryset()
        if self.request.GET.get('query', False):
            query = query.filter(Q(name__icontains=self.request.GET['query']) |
                                 Q(code__icontains=self.request.GET['query']))
        return query

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        if self.request.GET.get('query', False):
            context['query'] = self.request.GET['query']
        return context


class ServiceDetailView(DetailView):

    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        return context


class ServiceCreate(CreateView):
    model = Service
    form_class = CreateForm

    def get_context_data(self, **kwargs):
        context = super(ServiceCreate, self).get_context_data(**kwargs)
        return context


class ServiceUpdate(UpdateView):
    model = Service
    form_class = UpdateForm
    template_name = 'service/service_update_form.html'