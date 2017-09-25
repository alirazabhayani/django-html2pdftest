from django.conf.urls import url
from invoice.views import GeneratePdf,GeneratePdf2

urlpatterns = [
            url(r'^generate', GeneratePdf.as_view(),),\
            url(r'^generate2', GeneratePdf2.as_view(),)\
]

