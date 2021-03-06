from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Baymax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('woodpecker.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^woodpecker/', include('woodpecker.urls')),
    url(r'^news/', include('news.urls')),
	url(r'^nav/', include('news.urls')),
)
