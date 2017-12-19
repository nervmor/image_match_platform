# -*- coding: utf-8 -*-

import types
from urllib2 import URLError, HTTPError

from ..base.defn import *
from ..base.comm import *

import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .achieve import phash, template

@csrf_exempt
def phash_match(request):
    ret = {}

    while (True):
        res, ret, req= common_api_check(request)
        if (res != True):
            break
        ret['code'] = RESULT.PARAM_INVALID['code']
        ret['error'] = RESULT.PARAM_INVALID['error']
        try:
            url_src = req['url_src']
            url_dst = req['url_dst']
        except (TypeError, ValueError):
            break
        if len(url_src) == 0 or len(url_dst) == 0:
            break
        try:
            m = False
            r = {}
            for url_s in url_src:
                r_s = {}
                for url_d in url_dst:
                    re, dist = phash.match(url_s, url_d)
                    if re <> True:
                        continue
                    r_s[url_d] = dist
                    m = True
                r[url_s] = r_s
            if m == False:
                break
            ret['code'] = RESULT.SUCCESS['code']
            ret['results'] = r
            del ret['error']
            break
        except (TypeError, HTTPError, URLError, IOError):
            break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')


@csrf_exempt
def template_match(request):
    ret = {}

    while (True):
        res, ret, req= common_api_check(request)
        if (res != True):
            break
        ret['code'] = RESULT.PARAM_INVALID['code']
        ret['error'] = RESULT.PARAM_INVALID['error']
        try:
            url_src = req['url_src']
            url_dst = req['url_dst']
        except (TypeError, ValueError):
            break
        if len(url_src) == 0 or len(url_dst) == 0:
            break
        try:
            m = False
            r = {}
            for url_s in url_src:
                r_s = {}
                for url_d in url_dst:
                    re, locs = template.match(url_s, url_d)
                    if re <> True:
                        continue
                    r_s[url_d] = locs
                    m = True
                r[url_s] = r_s
            if m == False:
                break
            ret['code'] = RESULT.SUCCESS['code']
            ret['results'] = r
            del ret['error']
            break
        except (TypeError, HTTPError, URLError, IOError):
            break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')
