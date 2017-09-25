from django.conf.urls import patterns, include, url
from django_html2pdf.views import GeneratePdf,GeneratePdf2

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'html2pdf.views.home', name='home'),
    # url(r'^html2pdf/', include('html2pdf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^html2pdf/', include('django_html2pdf.urls')),
    url(r'^invoice/', include('invoice.urls')),
    url(r'^generate', GeneratePdf.as_view(),),
    url(r'^generate2', GeneratePdf2.as_view(),),
)
