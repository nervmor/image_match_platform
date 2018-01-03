import cv2
import numpy as np
import urllib2
from skimage import io

'''
def url_to_im(url, mode = 0):
    ret = False
    im = None
    try:
        r = urllib2.urlopen(url)
        im = np.asarray(bytearray(r.read()))
        im.astype(np.uint8)
        im = cv2.imdecode(im, mode)
        if im == None:
            raise TypeError
        ret = True
    except(TypeError, urllib2.HTTPError, urllib2.URLError, IOError):
        pass
    return ret, im
'''

def url_to_im(url):
    ret = False
    im = None
    try:
        im = io.imread(url)
        ret = True
    except(TypeError):
        pass
    return ret, im