# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from define import RESULT
from urllib2 import URLError, HTTPError

@csrf_exempt
def image_add(request):
    ret = {}
    url = ""
    metadata = ""

    while (True):
        res, ret, req= common_api_check(request)
        if (res != True):
            break
        try:
            url = req['url']
            metadata = req['metadata']
        except (TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['msg'] = RESULT.PARAM_INVALID['msg']
            break
        try:
            es = Elasticsearch()
            ses = SignatureES(es)
            ses.add_image(url, metadata=metadata)
            ret['code'] = RESULT.SUCCESS['code']
            ret['msg'] = RESULT.SUCCESS['msg']
            break
        except (TypeError, HTTPError, URLError, IOError):
            ret['code'] = RESULT.IMAGE_URL_INVALID['code']
            ret['msg'] = RESULT.IMAGE_URL_INVALID['msg']
            break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json')

@csrf_exempt
def image_match(request):
    ret = {}
    url = ""

    while (True):
        res, ret, req = common_api_check(request)
        if (res != True):
            break
        try:
            url = req['url']
        except (TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['msg'] = RESULT.PARAM_INVALID['msg']
            break
        try:
            es = Elasticsearch()
            ses = SignatureES(es)
            search_res = ses.search_image(url)
            r = []
            for sr in search_res:
                _r = {}
                _r['metadata'] = sr['metadata']
                _r['url'] = sr['path']
                _r['dist'] = sr['dist']
                r.append(_r)
            ret['code'] = RESULT.SUCCESS['code']
            ret['msg'] = RESULT.SUCCESS['msg']
            ret['result'] = r
            break
        except (TypeError, HTTPError, URLError, IOError):
            ret['code'] = RESULT.IMAGE_URL_INVALID['code']
            ret['msg'] = RESULT.IMAGE_URL_INVALID['msg']
            break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json')


def common_api_check(request):
    res = False
    ret = {}
    req = object
    while (True):
        if request.method != 'POST':
            ret['code'] = RESULT.HTTP_METHOD_NOT_SUPPORT['code']
            ret['msg'] = RESULT.HTTP_METHOD_NOT_SUPPORT['msg']
            break
        try:
            req = json.loads(request.body, encoding='utf-8')
            res = True
            break
        except (TypeError, ValueError, AttributeError), e:
            ret['code'] = RESULT.JSON_PARSE_ERROR['code']
            ret['msg'] = RESULT.JSON_PARSE_ERROR['msg']
            break
    return res, ret, req