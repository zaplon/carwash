from django.conf.urls import url

from contractor.views import ContractorListView, ContractorDetailView, ContractorCreate, ContractorUpdate, ContractorDelete

urlpatterns = [
    url(r'^$', ContractorListView.as_view(), name='contractor-list'),
    url(r'^dodaj/', ContractorCreate.as_view(), name='contractor-add'),
    url(r'^edytuj/(?P<pk>\d+)/$', ContractorUpdate.as_view(), name='contractor-edit'),
    url(r'^usun/(?P<pk>\d+)/$', ContractorDelete.as_view(), name='contractor-delete'),
    url(r'^(?P<pk>\d+)/$', ContractorDetailView.as_view(), name='contractor-detail'),

]