# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# -*- coding: utf-8 -*-
sys.path.append("..")
from common.common import *
from common.define import *
import types
from PIL import Image
import requests
from io import BytesIO
from . import models

def cacl_pic_ratio(wid, high):
    pic_ratio = float(wid) / float(high)
    pic_ratio = round(pic_ratio, 2)
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
            feat_x = req['feat_x']
            if not isinstance(feat_x, types.IntType) or feat_x < 0:
                break
            feat_y = req['feat_y']
            if not isinstance(feat_x, types.IntType) or feat_y < 0:
                break
            feat_x_range = req['feat_x_range']
            if not isinstance(feat_x_range, types.IntType):
                break
            feat_y_range = req['feat_y_range']
            if not isinstance(feat_y_range, types.IntType):
                break
            pic_url = req['pic_url']
            resp = requests.get(pic_url)
            pic = Image.open(BytesIO(resp.content))
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
                _feat_x=feat_x,
                _feat_y=feat_y,
                _feat_x_range=feat_y_range,
                _feat_y_range=feat_y_range,
                _pic_url=pic_url,
                _pic_wid = pic_wid,
                _pic_high = pic_high,
                _pic_ratio = pic_ratio,
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
                if not isinstance(pic_wid, types.IntType) or pic_wid < 0:
                    break
            if req.has_key('pic_high'):
                pic_high = req['pic_high']
                if not isinstance(pic_high, types.IntType) or pic_high < 0:
                    break

            pic_ratio = 0.0
            if not (pic_wid == 0 and pic_high == 0):
                if pic_wid * pic_high == 0:
                    ret['code'] = RESULT.PARAM_INVALID['code']
                    ret['error'] = RESULT.PARAM_INVALID['error']
                    break
                pic_ratio = cacl_pic_ratio(pic_wid, pic_high)
            if pic_ratio == 0.0:
                qr = models.phash_feature.objects.all().values(
                    '_pic_url',
                    '_pic_wid',
                    '_pic_high',
                    '_pic_ratio',
                    '_feat_x',
                    '_feat_y',
                    '_feat_x_range',
                    '_feat_y_range',
                    '_metadata'
                )
            else:
                qr = models.phash_feature.objects.filter(_pic_ratio=pic_ratio).values(
                    '_pic_url',
                    '_pic_wid',
                    '_pic_high',
                    '_pic_ratio',
                    '_feat_x',
                    '_feat_y',
                    '_feat_x_range',
                    '_feat_y_range',
                    '_metadata'
                )
            ret['code'] = RESULT.SUCCESS['code']
            ret['data'] = []
            for r in qr:
                entry = {}
                entry['pic_url'] = r['_pic_url']
                entry['pic_wid'] = r['_pic_wid']
                entry['pic_high'] = r['_pic_high']
                entry['pic_ratio'] = r['_pic_ratio']
                entry['feat_x'] = r['_feat_x']
                entry['feat_y'] = r['_feat_y']
                entry['feat_x_range'] = r['_feat_x_range']
                entry['feat_y_range'] = r['_feat_y_range']
                entry['metadata'] = r['_metadata']
                ret['data'].append(entry)
        except (KeyError, TypeError, ValueError):
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']
            break
        break
    if ret['code'] != RESULT.SUCCESS['code']:
        return HttpResponseBadRequest(json.dumps(ret), content_type='application/json;')
    else:
        return HttpResponse(json.dumps(ret), content_type='application/json;')