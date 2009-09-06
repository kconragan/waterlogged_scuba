from django.conf.urls.defaults import *

# Django Admin Utility
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^waterlogged/', include('waterlogged.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    # Session Management
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
)
