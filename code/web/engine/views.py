# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
from image_match.goldberg import ImageSignature
import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from define import RESULT
from urllib2 import URLError, HTTPError
import types

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
            if req.has_key('metadata'):
                metadata = req['metadata']
        except (TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']
            break
        try:
            es = Elasticsearch()
            ses = SignatureES(es)
            ses.add_image(url, metadata=metadata)
            ret['code'] = RESULT.SUCCESS['code']
            break
        except (TypeError, HTTPError, URLError, IOError):
            ret['code'] = RESULT.IMAGE_URL_INVALID['code']
            ret['error'] = RESULT.IMAGE_URL_INVALID['error']
            break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')

@csrf_exempt
def image_remove(request):
    ret = {}
    url = ""

    while (True):
        res, ret, req= common_api_check(request)
        if (res != True):
            break
        try:
            url = req['url']
        except (TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']
            break
        try:
            es = Elasticsearch()
            ses = SignatureES(es)
            del_cnt = ses.delete_record_by_path(url)
            ret['code'] = RESULT.SUCCESS['code']
            ret['result'] = {'delcnt': del_cnt}
            break
        except (TypeError, HTTPError, URLError, IOError):
            ret['code'] = RESULT.IMAGE_URL_INVALID['code']
            ret['error'] = RESULT.IMAGE_URL_INVALID['error']
            break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json')


@csrf_exempt
def image_match(request):
    ret = {}

    while (True):
        res, ret, req= common_api_check(request)
        if (res != True):
            break
        try:
            url_src = req['url_src']
            url_dst = req['url_dst']
        except (TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']
            break
        try:
            r = {}
            for url_s in url_src:
                r_s = {}
                for url_d in url_dst:
                    gis = ImageSignature()
                    dist = gis.normalized_distance(gis.generate_signature(url_s), gis.generate_signature(url_d))
                    r_s[url_d] = dist
                r[url_s] = r_s

            ret['code'] = RESULT.SUCCESS['code']
            ret['result'] = r
            break
        except (TypeError, HTTPError, URLError, IOError):
            ret['code'] = RESULT.IMAGE_URL_INVALID['code']
            ret['error'] = RESULT.IMAGE_URL_INVALID['error']
            break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')

@csrf_exempt
def image_search(request):
    ret = {}
    url = ""
    maxdist = 0.0
    while (True):
        res, ret, req = common_api_check(request)
        if (res != True):
            break
        try:
            url = req['url']
            if req.has_key('maxdist'):
                maxdist = req['maxdist']
                if not isinstance(maxdist, types.FloatType):
                    ret['code'] = RESULT.MAXDIST_INVALID['code']
                    ret['error'] = RESULT.MAXDIST_INVALID['error']
                    break
        except (TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']
            break
        try:
            es = Elasticsearch()
            if maxdist != 0.0:
                ses = SignatureES(es, distance_cutoff=maxdist)
            else:
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
            ret['result'] = r
            break
        except (TypeError, HTTPError, URLError, IOError):
            ret['code'] = RESULT.IMAGE_URL_INVALID['code']
            ret['error'] = RESULT.IMAGE_URL_INVALID['error']
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
            ret['error'] = RESULT.HTTP_METHOD_NOT_SUPPORT['error']
            break
        try:
            req = json.loads(request.body, encoding='utf-8')
            res = True
            break
        except (TypeError, ValueError, AttributeError), e:
            ret['code'] = RESULT.JSON_PARSE_ERROR['code']
            ret['error'] = RESULT.JSON_PARSE_ERROR['error']
            break
    return res, ret, req