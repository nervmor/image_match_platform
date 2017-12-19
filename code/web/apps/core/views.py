# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.
# Create your views here.
# -*- coding: utf-8 -*-

from ..base.defn import *
from ..base.comm import *

import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import types
from frame import checker
from .defn.define import *
@csrf_exempt
def check(request):
    ret = {}

    while (True):
        res, ret, req = common_api_check(request)
        if (res != True):
            break
        ret['code'] = RESULT.PARAM_INVALID['code']
        ret['error'] = RESULT.PARAM_INVALID['error']
        if not req.has_key('pic_url') or not is_type_str(req['pic_url']):
            break
        pic_url = req['pic_url']
        if req.has_key('category'):
            category = req['category']
            if not is_type_str(category):
                break
        else:
            category = 'default'

        chker = checker.checker(category, pic_url)
        r, d = chker.run()
        if r <> res_succs:
            break
        matched = False
        if len(d['phash']) <> 0 or len(d['template']) <> 0:
           matched = True
        s = {}
        s['matched'] = matched
        s['detail'] = d
        ret['results'] = s
        ret['code'] = RESULT.SUCCESS['code']
        del ret['error']
        break

    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')