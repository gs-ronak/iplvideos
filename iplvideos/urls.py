from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp.views import sample_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iplvideos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^sample/', sample_view),
    (r'^app/', include('myapp.urls'))
)

urlpatterns += staticfiles_urlpatterns()
