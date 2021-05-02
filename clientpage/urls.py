from django.urls import path
from pdfsite import urls
from . import  views
urlpatterns = [
    path("clientpage", views.clientpage),
    path("contentlist", views.ListPdf.as_view(), name="contentlist"),
    path('<slug:slug>', views.DistPdf.as_view(), name='pdfDetail'),   
]