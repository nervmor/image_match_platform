import requests
import common
import logging
from ..defn.define import *

class template_interface:
    def __init__(self, engine_srv_ip, feature_srv_ip):
        self._engine_srv_ip = engine_srv_ip
        self._feature_srv_ip = feature_srv_ip
        pass

    def match(self, url_src, url_dst):
        ret = res_fail
        res = []
        while (True):

            req_data = {}
            req_data['url_src'] = []
            req_data['url_src'].append(url_src)
            req_data['url_dst'] = []
            req_data['url_dst'].append(url_dst)
            url = "http://" + self._engine_srv_ip + "/api/engine/template/match/"
            code, err, data = common.request(url, req_data)
            if code <> 200:
                logging.getLogger('all').error('request src[%s] dst[%s] fail with code[%d] error[%s]',
                                                 url_src, url_dst, code, err)
                break
            if not data:
                logging.getLogger('all').error('request src[%s] dst[%s] respond data is none',
                                                 url_src, url_dst)
                break
            if len(data) != 1:
                logging.getLogger('all').error('request src[%s] dst[%s] respond data is invalid',
                                                 url_src, url_dst)
                break
            r_s = data[url_src]
            if len(r_s) != 1:
                logging.getLogger('all').error('request src[%s] dst[%s] respond data is invalid',
                                                 url_src, url_dst)
                break
            ret = res_succs
            res = r_s[url_dst]
            break
        return ret, res

    def feature_get(self, cls, pic_wid, pic_high):
        data = {}
        req_data = {}
        req_data['class'] = cls
        req_data['pic_wid'] = pic_wid
        req_data['pic_high'] = pic_high
        url = "http://" + self._feature_srv_ip + "/api/feature/template/get/"
        code, err, data = common.request(url, req_data)
        if code <> 200:
            logging.getLogger('all').error('request pic_wid[%d] pic_high[%d] fail with code[%d] error[%s]',
                                                 pic_wid, pic_high, code, err)
            return res_fail, data
        return res_succs, data