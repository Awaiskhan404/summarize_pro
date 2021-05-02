from django.forms import forms

class UploadedPdf(forms.Form):
   pdffile = forms.FileField 