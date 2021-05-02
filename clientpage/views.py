from django.shortcuts import render, redirect
from .forms import UploadedPdf
from .models import ListViewPdf
from PyPDF2 import PdfFileReader
from django.core import files
from django.views.generic import ListView, DetailView
from pdfsite import settings



def clientpage(request):
    nump = None
    current_user = request.user
    current_email = None
    context = {}
    if request.method == 'POST':
        form = UploadedPdf(request.POST, request.FILES)
        if form.is_valid():
            if '.pdf' in request.FILES['pdf'].name:
                current_email = current_user.email
                context['form'] = form
                dir_pdffile = 'media/'+request.FILES['pdf'].name
                file = request.FILES['pdf']
                with open(dir_pdffile, 'wb+') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                with open(dir_pdffile, 'rb') as pdf_file:
                    pdf_reader = PdfFileReader(pdf_file)
                    nump = pdf_reader.numPages 
                total = nump * settings.PDF_PRICE_PAGE             
                instance = ListViewPdf(pdffile=request.FILES['pdf'], email=current_email, name = request.FILES['pdf'].name, number_page = nump, total_price = total)
                instance.save()
                return redirect('/contentlist')
            else:
                form = UploadedPdf()
        else:
            form = UploadedPdf()
    return render(request, "client.html", context)


class ListPdf(ListView):
    models = ListViewPdf    
    def get_queryset(self):
        return ListViewPdf.objects.order_by('name')

class DistPdf(DetailView):
    models = ListViewPdf
    def get_queryset(self):
        return ListViewPdf.objects




    
