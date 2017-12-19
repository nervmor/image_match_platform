# -*- coding: utf-8 -*-

from urllib2 import URLError, HTTPError
from image_match.goldberg import ImageSignature

def match(url_s, url_d):
    try:
        gis = ImageSignature()
        sgin_s = gis.generate_signature(url_s)
        sgin_d = gis.generate_signature(url_d)
        dist = gis.normalized_distance(sgin_s, sgin_d)
    except (TypeError, HTTPError, URLError, IOError):
        return False, -1.0
    return True, dist