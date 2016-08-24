from django.conf.urls import url

from service.views import ServiceListView, ServiceDetailView, ServiceCreate, ServiceUpdate, service_as_json

urlpatterns = [
    url(r'^$', ServiceListView.as_view(), name='service-list'),
    url(r'^dodaj/', ServiceCreate.as_view(), name='service-add'),
    url(r'^edytuj/(?P<pk>\d+)/$', ServiceUpdate.as_view(), name='service-edit'),
    url(r'^(?P<pk>\d+)/$', ServiceDetailView.as_view(), name='service-detail'),
    url(r'^json/', service_as_json, name='service-json'),
]