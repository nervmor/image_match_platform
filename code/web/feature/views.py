# -*- coding: utf-8 -*-
from __future__ import unicode_literals



import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# -*- coding: utf-8 -*-
from common.define import *
from common.common import *
import types
from PIL import Image
import requests
from io import BytesIO
from . import models


def cacl_pic_ratio(wid, high):
    pic_ratio = float(wid) / float(high)
    pic_ratio = round(pic_ratio, 1)
    return pic_ratio


@csrf_exempt
def phash_feature_add(request):
    ret = {}

    while (True):
        res, ret, req = common_api_check(request)
        if (res != True):
            break
        try:
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']
            if not req.has_key('category') or not is_type_str(req['category']):
                category = 'default'
            else:
                category = req['category']
            if not req.has_key('pic_url') or not is_type_str(req['pic_url']):
                break
            pic_url = req['pic_url']
            if req.has_key('dist'):
                if not is_type_float(req['dist']) or req['dist'] < 0:
                    break
                dist = req['dist']
            else:
                dist = -1.0
            if not req.has_key('feat_x'):
                break
            feat_x = req['feat_x']
            if not is_type_int(feat_x) or feat_x < 0:
                break
            if not req.has_key('feat_y'):
                break
            feat_y = req['feat_y']
            if not is_type_int(feat_y) or feat_y < 0:
                break
            if not req.has_key('feat_w'):
                break
            feat_w = req['feat_w']
            if not is_type_int(feat_w) or feat_w < 0:
                break
            if not req.has_key('feat_h'):
                break
            feat_h = req['feat_h']
            if not is_type_int(feat_h) or feat_h < 0:
                break
            if not req.has_key('feat_x_range'):
                break
            feat_x_range = req['feat_x_range']
            if not is_type_int(feat_x_range):
                break
            if not req.has_key('feat_y_range'):
                break
            feat_y_range = req['feat_y_range']
            if not is_type_int(feat_y_range):
                break

            try:
                resp = requests.get(pic_url)
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.HTTPError,
                    requests.exceptions.Timeout,
                    requests.exceptions.TooManyRedirects):
                break
            if resp.status_code <> 200:
                break
            try:
                pic = Image.open(BytesIO(resp.content))
            except(IOError):
                break
            pic_wid = pic.size[0]
            pic_high = pic.size[1]
            pic_ratio = cacl_pic_ratio(pic_wid, pic_high)
            if feat_x + feat_x_range > pic_wid:
                break
            if feat_y + feat_y_range > pic_high:
                break
            metadata = ""
            if req.has_key('metadata'):
                metadata = req['metadata']


            qr = models.phash_feature.objects.get_or_create(
                _category=category,
                _feat_x=feat_x,
                _feat_y=feat_y,
                _feat_w=feat_w,
                _feat_h=feat_h,
                _feat_x_range=feat_y_range,
                _feat_y_range=feat_y_range,
                _pic_url=pic_url,
                _pic_wid = pic_wid,
                _pic_high = pic_high,
                _pic_ratio = pic_ratio,
                _dist = dist,
                _metadata=metadata)
            ret['code'] = RESULT.SUCCESS['code']
            del ret['error']
        except (KeyError, TypeError, ValueError):
            break
        except (IOError):
            ret['code'] = RESULT.IMAGE_URL_INVALID['code']
            ret['error'] = RESULT.IMAGE_URL_INVALID['error']
            break
        break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')


@csrf_exempt
def phash_feature_get(request):
    ret = {}

    while (True):
        res, ret, req = common_api_check(request)
        if (res != True):
            break
        try:
            pic_wid = 0
            pic_high = 0
            if req.has_key('pic_wid'):
                pic_wid = req['pic_wid']
                if not is_type_int(pic_wid) or pic_wid < 0:
                    break
            if req.has_key('pic_high'):
                pic_high = req['pic_high']
                if not is_type_int(pic_high) or pic_high < 0:
                    break
            if req.has_key('category'):
                category = req['category']
                if not is_type_str(category):
                    break
            else:
                category = 'default'

            pic_ratio = 0.0
            if not (pic_wid == 0 and pic_high == 0):
                if pic_wid * pic_high == 0:
                    ret['code'] = RESULT.PARAM_INVALID['code']
                    ret['error'] = RESULT.PARAM_INVALID['error']
                    break
                pic_ratio = cacl_pic_ratio(pic_wid, pic_high)

            if pic_ratio == 0.0:
                qr = models.phash_feature.all().filter(_category=category).values(
                    '_pic_url',
                    '_pic_wid',
                    '_pic_high',
                    '_pic_ratio',
                    '_feat_x',
                    '_feat_y',
                    '_feat_w',
                    '_feat_h',
                    '_feat_x_range',
                    '_feat_y_range',
                    '_dist',
                    '_metadata'
                )
            else:
                qr = models.phash_feature.objects.filter(_category=category, _pic_ratio=pic_ratio).values(
                    '_pic_url',
                    '_pic_wid',
                    '_pic_high',
                    '_pic_ratio',
                    '_feat_x',
                    '_feat_y',
                    '_feat_w',
                    '_feat_h',
                    '_feat_x_range',
                    '_feat_y_range',
                    '_dist',
                    '_metadata'
                )
            ret['code'] = RESULT.SUCCESS['code']
            ret['results'] = []
            for r in qr:
                entry = {}
                entry['pic_url'] = r['_pic_url']
                entry['pic_wid'] = r['_pic_wid']
                entry['pic_high'] = r['_pic_high']
                entry['pic_ratio'] = r['_pic_ratio']
                entry['feat_x'] = r['_feat_x']
                entry['feat_y'] = r['_feat_y']
                entry['feat_w'] = r['_feat_w']
                entry['feat_h'] = r['_feat_h']
                entry['feat_x_range'] = r['_feat_x_range']
                entry['feat_y_range'] = r['_feat_y_range']
                entry['dist'] = r['_dist']
                entry['metadata'] = r['_metadata']
                ret['results'].append(entry)
        except (KeyError, TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']
            break
        break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')