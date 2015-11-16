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
import json

# Create your views here.

def codelist(request):
    code_list_src = []
    code_list_src = KLineCodeList.objects.filter(ktype='5')#.values('code', 'name').values_list()
    code_list = []
    for rec in code_list_src:
        code_list.append({'label':rec.code+'-'+rec.name, 'value':rec.code})
    data = json.dumps(code_list)
    return HttpResponse(data, mimetype="application/json")

def klinedata(request, code, ktype):
    print code, ktype
    kl_data = []
    kl_data = KLine.objects.filter(code = code, ktype= ktype)
    kl_data_pure = []
    for rec in kl_data:
        one = {
            'timestamp':rec.timestamp,
            'open': rec.open,
            'high': rec.high,
            'low': rec.low,
            'close': rec.close,
            'volume': rec.volume,
        }
        kl_data_pure.append(one)

    # data = serializers.serialize("json", kl_data)
    data = json.dumps(kl_data_pure)
    return HttpResponse(data)
