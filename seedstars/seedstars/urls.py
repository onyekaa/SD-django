from django.conf.urls import include, url
from django.contrib import admin
from contacts import views as contact_views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="contacts/index.html")),
    url(r'^add/$', contact_views.add, name='add_contacts'),
    url(r'^edit/(?P<id>[0-9]+)/$', contact_views.add, name='edit_contact'),
    url(r'^list/$', contact_views.list, name='list_contacts'),
]
