from django.conf.urls import url

from invoice.views import InvoiceListView, InvoiceDetailView, InvoiceCreate, InvoiceUpdate

urlpatterns = [
    url(r'^$', InvoiceListView.as_view(), name='invoice-list'),
    url(r'^dodaj/', InvoiceCreate.as_view(), name='invoice-add'),
    url(r'^edytuj/(?P<pk>[-\w]+)/$', InvoiceUpdate.as_view(), name='invoice-edit'),
    url(r'^(?P<pk>[-\w]+)/$', InvoiceDetailView.as_view(), name='invoice-detail'),
]