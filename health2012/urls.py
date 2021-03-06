from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^mine/$', 'mine.views.index'),
    url(r'^mine/index$', 'mine.views.index'),
    url(r'^mine/display', 'mine.views.display'),
    url(r'^mine/form', 'mine.views.form'),
    url(r'^mine/field_filter$', 'mine.views.field_filter'),
    url(r'^mine/ajax_handler$', 'mine.views.ajax_handler'),
    # url(r'^$', 'health2012.views.home', name='home'),
    # url(r'^health2012/', include('health2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
