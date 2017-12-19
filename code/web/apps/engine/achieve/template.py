from .util import *
import cv2
import numpy as np


def match(url_s, url_d):
    ret = False,
    res = []
    while (True):
        r, im_s = url_to_im(url_s)
        if r <> True:
            break
        r, im_d = url_to_im(url_d)
        if r <> True:
            break
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        for meth in methods:
            method = eval(meth)
            re = cv2.matchTemplate(im_s, im_d, method)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(re)

            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                loc = min_loc
            else:
                loc = max_loc
            res.append(loc)
        ret = True
        break
    return ret, res