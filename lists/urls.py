from django.conf.urls import patterns, include, url
from lists_app import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^home$', views.home, name='home'),
                       url(r'^create$', views.create_order, name='create_order'),
                       url(r'^create-item$', views.create_item, name='create_item'),
                       url(r'^update-order/(\d+)$', views.update_order, name='update_order'),

                       # Examples:
                       # url(r'^$', 'lists.views.home', name='home'),
                       # url(r'^lists/', include('lists.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
)
