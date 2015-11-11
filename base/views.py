#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   liqiang
#   E-mail  :   liqiang@prettydad.com
#   Date    :   15/11/11 23:42:36
#   Desc    :   The views of the base module

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from models import KLine, KLineCodeList

# Create your views here.

def home(request):
    return render(request, 'base/home.tpl', {})

def kline(request):
    code_list_src = []
    code_list_src = KLineCodeList.objects.filter(ktype='5')
    code_list = []
    for rec in code_list_src:
        one_item = {}
        one_item['label'] = rec.code + '-' + rec.name
        one_item['value'] = rec.code
        code_list.append(one_item)
    return render(request, 'base/kline.tpl', {'code_list': code_list_src})

def klinedata(request, code, ktype):
    print code, ktype
    kl_data = []
    kl_data = KLine.objects.filter(code = code, ktype= ktype)

    data = serializers.serialize("json", kl_data)
    return HttpResponse(data)

def kline_code_get(request):
    return HttpResponse()
