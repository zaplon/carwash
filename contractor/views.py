from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Contractor
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateForm
from django.db.models import Q


class ContractorListView(ListView):

    model = Contractor
    paginate_by = 10

    def get_queryset(self):
        query = super(ContractorListView, self).get_queryset()
        if self.request.GET.get('query', False):
            query = query.filter(Q(name__icontains=self.request.GET['query']) |
                                 Q(nip__icontains=self.request.GET['query']))
        return query

    def get_context_data(self, **kwargs):
        context = super(ContractorListView, self).get_context_data(**kwargs)
        if self.request.GET.get('query', False):
            context['query'] = self.request.GET['query']
        return context


class ContractorDetailView(DetailView):

    model = Contractor

    def get_context_data(self, **kwargs):
        context = super(ContractorDetailView, self).get_context_data(**kwargs)
        return context


class ContractorCreate(CreateView):
    model = Contractor
    form_class = CreateForm


class ContractorUpdate(UpdateView):
    model = Contractor
    form_class = CreateForm


class ContractorDelete(DeleteView):
    model = Contractor
    success_url = reverse_lazy('contractor-list')
