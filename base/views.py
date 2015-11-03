from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from models import KLine

# Create your views here.

def home(request):
    return render(request, 'base/home.tpl', {})

def kline(request):
    return render(request, 'base/kline.tpl', {})

def klinedata(request, code, ktype):
    print code, ktype
    kl_data = []
    kl_data = KLine.objects.filter(code = code, ktype= ktype)

    data = serializers.serialize("json", kl_data)
    return HttpResponse(data)

def kline_code_get(request):
