from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView



urlpatterns = patterns('',

		url(r'^home$', TemplateView.as_view(template_name='myapp/index.html'), name="home"),
)
