from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'joinourstorywebsite.views.home', name='home'),
                       # url(r'^joinourstorywebsite/', include('joinourstorywebsite.foo.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'contactus$', 'joinourstorywebsitebase.views.contactus', name='contactus'),
                       url(r'index', 'joinourstorywebsitebase.views.index', name = 'index'),
                       url(r'^$', 'joinourstorywebsitebase.views.index', name='index'), ### change!
                       )
