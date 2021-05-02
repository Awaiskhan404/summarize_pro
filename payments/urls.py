from django.urls import path
from pdfsite import urls
from . import views

urlpatterns = [
    path("",views.payment, name='payment' )
]