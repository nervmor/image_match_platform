# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import json
from django.http import HttpResponse, HttpResponseBadRequest


def image_add(request):
    ret = {}
    if request.method != 'POST':
        ret['code'] = -1
        ret['msg'] = 'only POST method support'
        return HttpResponseBadRequest("ret")

    req = json.loads(request.raw_post_data)

    return HttpResponse("image_add_ok")


def image_match(request):
    return HttpResponse("image_match_ok")