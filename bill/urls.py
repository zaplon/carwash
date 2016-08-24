from django.conf.urls import url

from bill.views import BillListView, BillDetailView, BillCreate, BillUpdate

urlpatterns = [
    url(r'^$', BillListView.as_view(), name='bill-list'),
    url(r'^dodaj/', BillCreate.as_view(), name='bill-add'),
    url(r'^edytuj/(?P<slug>[-\w]+)/$', BillUpdate.as_view(), name='bill-edit'),
    url(r'^(?P<slug>[-\w]+)/$', BillDetailView.as_view(), name='bill-detail'),
]