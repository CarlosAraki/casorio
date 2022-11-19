from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pdb


# Create your views here.
# vercel-django-example/example/views.py
# https://github.com/jayhale/vercel-django-example/blob/main/example/views.py#L6

import datetime
from django.http import HttpResponse, JsonResponse

def index(request):
    now = datetime.datetime.now() - datetime.timedelta(hours = 3)
    casorio = datetime.datetime(year= 2023, month= 7, day= 28, hour = 18)
    
    faltam = casorio - now
    faltam_dias = faltam.days
    faltam_horas = faltam.seconds//3600
    faltam_minutos = (faltam.seconds//60)%60
    faltam_segundos = faltam.seconds - faltam_horas*60*60 - faltam_minutos*60

    context = {}

    context['dias'] = faltam_dias
    context['horas'] = faltam_horas
    context['minutos'] = faltam_minutos
    context['segundos'] = faltam_segundos     

    return render(request, 'home.html', context = context)

@csrf_exempt
def update_clock(request):
    now = datetime.datetime.now() - datetime.timedelta(hours = 3)
    casorio = datetime.datetime(year= 2023, month= 7, day= 28, hour = 18)
    
    faltam = casorio - now
    faltam_dias = faltam.days
    faltam_horas = faltam.seconds//3600
    faltam_minutos = (faltam.seconds//60)%60
    faltam_segundos = faltam.seconds - faltam_horas*60*60 - faltam_minutos*60
    
    data = {}

    data['dias'] = faltam_dias
    data['horas'] = faltam_horas
    data['minutos'] = faltam_minutos
    data['segundos'] = faltam_segundos     

    print(data)
    return JsonResponse(data)

def login(request):

    return render(request, 'login.html')