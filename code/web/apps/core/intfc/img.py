import requests
import logging
from PIL import Image
import requests
from io import BytesIO
from ..defn.define import *
import types

class img_info:
    def __init__(self, width, height, url):
        self._width = width
        self._height = height
        self._url = url

class img_interface:
    def __init__(self):
        pass
    def fetch(self, pic_url):
        ret = res_fail
        info = {}

        while (True):
            try:
                r = requests.get(url = pic_url)
            except (requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                requests.exceptions.Timeout,
                requests.exceptions.TooManyRedirects):
                break

            if r.status_code <> 200:
                logging.getLogger('all').error('img fetch url[%s] fail with code[%d]',
                                                 pic_url, r.code)
                break
            try:
                pic = Image.open(BytesIO(r.content))
            except(IOError):
                break
            pic_wid = pic.size[0]
            pic_high = pic.size[1]
            info = img_info(pic_wid, pic_high, pic_url)
            ret = res_succs
            break
        return ret, info

    def gen_url(self, url, x = -1, y = -1, w = -1, h = -1):
        pic_url = ""
        args = ""
        if not isinstance(x, types.IntType):
            return res_argv_err, ""
        if not isinstance(y, types.IntType):
            return res_argv_err, ""
        if not isinstance(w, types.IntType):
            return res_argv_err, ""
        if not isinstance(h, types.IntType):
            return res_argv_err, ""
        if not (x == -1 and y == -1 and w == -1 and h == -1):
            if x == -1 or y == -1 or w == -1 or h == -1:
                return res_argv_err, ""
            else:
                args += "x=" + str(x)
                args += "&y=" + str(y)
                args += "&w=" + str(w)
                args += "&h=" + str(h)
                args += "&g=" + str(1)
        pic_url = url
        if len(args) <> 0:
            pic_url += "?" + args
        return res_succs, pic_url
