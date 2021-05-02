from django.shortcuts import render
from django.shortcuts import redirect
from clientpage.models import ListViewPdf
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def payment(request):
    body = json.loads(request.body)
    ida = body['acepted']
    ListViewPdf.objects.filter(pk=ida).update(is_paid = True)
    return redirect('/contentlist')
    
    