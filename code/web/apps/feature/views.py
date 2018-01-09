# -*- coding: utf-8 -*-
from __future__ import unicode_literals



import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# -*- coding: utf-8 -*-
from ..base.defn import *
from ..base.comm import *
import types
from PIL import Image
import requests
from io import BytesIO
from . import models
from django.db.models import Q
import operator



def cacl_pic_ratio(wid, high):
    pic_ratio = float(wid) / float(high)
    pic_ratio = round(pic_ratio, 1)
    return pic_ratio


def int_valid(req, key):
    if not req.has_key(key):
        return False
    if not is_type_int(req[key]):
        return False
    if req[key] < 0:
        return False
    return True

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

            r, category, tags= parse_class_param(req)
            if r <> True:
                break

            str_category, str_tags = make_pic_class_str(category, tags)

            if not req.has_key('pic_url') or not is_type_str(req['pic_url']):
                break
            pic_url = req['pic_url']
            dist = -1.0
            if req.has_key('dist'):
                if not is_type_float(req['dist']) or req['dist'] < 0:
                    break
                dist = req['dist']
            if not int_valid(req, 'feat_x'):
                break
            feat_x = req['feat_x']
            if not int_valid(req, 'feat_y'):
                break
            feat_y = req['feat_y']
            if not int_valid(req, 'feat_w'):
                break
            feat_w = req['feat_w']
            if not int_valid(req, 'feat_h'):
                break
            feat_h = req['feat_h']
            if not int_valid(req, 'feat_x_range'):
                break
            feat_x_range = req['feat_x_range']
            if not int_valid(req, 'feat_y_range'):
                break
            feat_y_range = req['feat_y_range']

            metadata = ""
            if req.has_key('metadata'):
                if not is_type_str(req['metadata']):
                    break
                metadata = req['metadata']
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

            qr = models.phash_feature.objects.get_or_create(
                _category=str_category,
                _tags=str_tags,
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
                _metadata= metadata)
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
            r, category, tags= parse_class_param(req)
            if r <> True:
                break

            pic_ratio = 0.0
            if not (pic_wid == 0 and pic_high == 0):
                if pic_wid * pic_high == 0:
                    ret['code'] = RESULT.PARAM_INVALID['code']
                    ret['error'] = RESULT.PARAM_INVALID['error']
                    break
                pic_ratio = cacl_pic_ratio(pic_wid, pic_high)

            category_q_list = []
            for obj in category:
                q_obj = Q(**{"_category__contains": obj})
                category_q_list.append(q_obj)
            tags_q_list = []
            for obj in tags:
                q_obj = Q(**{"_tags__contains": obj})
                tags_q_list.append(q_obj)

            query = Q(**{})
            if len(category_q_list) <> 0:
                query = query & reduce(operator.or_, category_q_list)
            if len(tags_q_list) <> 0:
                query = query & reduce(operator.or_, tags_q_list)
            if pic_ratio <> 0.0:
                query = query & Q(_pic_ratio=pic_ratio)

            qr = models.phash_feature.objects.filter(query).values(
                    '_category',
                    '_tags',
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
                entry['class'] = make_pic_class(r['_category'], r['_tags'])
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


@csrf_exempt
def template_feature_add(request):
    ret = {}

    while (True):
        res, ret, req = common_api_check(request)
        if (res != True):
            break
        try:
            ret['code'] = RESULT.PARAM_INVALID['code']
            ret['error'] = RESULT.PARAM_INVALID['error']

            r, category, tags= parse_class_param(req)
            if r <> True:
                break
            str_category, str_tags = make_pic_class_str(category, tags)

            if not req.has_key('pic_url') or not is_type_str(req['pic_url']):
                break
            pic_url = req['pic_url']

            if not int_valid(req, 'feat_x'):
                break
            feat_x = req['feat_x']
            if not int_valid(req, 'feat_y'):
                break
            feat_y = req['feat_y']
            if not int_valid(req, 'feat_w'):
                break
            feat_w = req['feat_w']
            if not int_valid(req, 'feat_h'):
                break
            feat_h = req['feat_h']

            if req.has_key('deva'):
                if not is_type_int(req['deva']) or req['deva'] < 0:
                    break
                deva = req['deva']
            else:
                deva = -1
            if req.has_key('mcnt'):
                if not is_type_int(req['mcnt']) or req['mcnt'] < 0 or req['mcnt'] > 6:
                    break
                mcnt = req['mcnt']
            else:
                mcnt = -1
            if req.has_key('dist'):
                if not is_type_float(req['dist']) or req['dist'] < 0:
                    break
                dist = req['dist']
            else:
                dist = -1.0
            metadata = ""
            if req.has_key('metadata'):
                if not is_type_str(req['metadata']):
                    break
                metadata = req['metadata']
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
            if deva <> -1:
                if deva > pic_wid:
                    break
                if deva > pic_high:
                    break

            qr = models.template_feature.objects.get_or_create(
                _category=str_category,
                _tags=str_tags,
                _pic_url=pic_url,
                _pic_wid=pic_wid,
                _pic_high=pic_high,
                _pic_ratio=pic_ratio,
                _feat_x=feat_x,
                _feat_y=feat_y,
                _feat_w=feat_w,
                _feat_h=feat_h,
                _deva=deva,
                _mcnt=mcnt,
                _dist=dist,
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
def template_feature_get(request):
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
            r, category, tags= parse_class_param(req)
            if r <> True:
                break

            if not (pic_wid == 0 and pic_high == 0):
                if pic_wid * pic_high == 0:
                    ret['code'] = RESULT.PARAM_INVALID['code']
                    ret['error'] = RESULT.PARAM_INVALID['error']
                    break

            category_q_list = []
            for obj in category:
                q_obj = Q(**{"_category__contains": obj})
                category_q_list.append(q_obj)
            tags_q_list = []
            for obj in tags:
                q_obj = Q(**{"_tags__contains": obj})
                tags_q_list.append(q_obj)

            query = Q(**{})
            if len(category_q_list) <> 0:
                query = query & reduce(operator.or_, category_q_list)
            if len(tags_q_list) <> 0:
                query = query & reduce(operator.or_, tags_q_list)
            if pic_wid * pic_high <> 0.0:
                query = query & Q(_feat_w__lte=pic_wid, _feat_h__lte=pic_high)

            qr = models.template_feature.objects.filter(query).values(
                    '_category',
                    '_tags',
                    '_pic_url',
                    '_pic_wid',
                    '_pic_high',
                    '_feat_x',
                    '_feat_y',
                    '_feat_w',
                    '_feat_h',
                    '_deva',
                    '_mcnt',
                    '_dist',
                    '_metadata'
                )
            ret['code'] = RESULT.SUCCESS['code']
            ret['results'] = []
            for r in qr:
                entry = {}
                entry['class'] = make_pic_class(r['_category'], r['_tags'])
                entry['pic_url'] = r['_pic_url']
                entry['pic_wid'] = r['_pic_wid']
                entry['pic_high'] = r['_pic_high']
                entry['feat_x'] = r['_feat_x']
                entry['feat_y'] = r['_feat_y']
                entry['feat_w'] = r['_feat_w']
                entry['feat_h'] = r['_feat_h']
                entry['deva'] = r['_deva']
                entry['mcnt'] = r['_mcnt']
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