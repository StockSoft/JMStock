#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   liqiang
#   E-mail  :   liqiang@prettydad.com
#   Date    :   15/11/11 23:42:36
#   Desc    :   The views of the web module

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def home(request):
    return render(request, 'web/home.tpl', {})

def kline(request):
    '''
    code_list_src = []
    code_list_src = KLineCodeList.objects.filter(ktype='5')
    code_list = []
    for rec in code_list_src:
        one_item = {}
        one_item['label'] = rec.code + '-' + rec.name
        one_item['value'] = rec.code
        code_list.append(one_item)
    '''
    # return render(request, 'web/kline.tpl', {'code_list': code_list_src})
    return render(request, 'web/kline.tpl', {})
