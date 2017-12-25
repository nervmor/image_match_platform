from ..intfc import img
from ..intfc import template
from .. import conf
import logging
from ..defn.define import *

class template_check_task:
    def __init__(self, template_itfc, img_itfc, cls, pic_info):
        self._template_itfc = template_itfc
        self._img_itfc = img_itfc
        self._cls = cls
        self._pic_info = pic_info


    def match_feature(self, pic_info, feat):
        ret = res_fail
        data = []
        ret, feat_url = self._img_itfc.gen_url(
            feat['pic_url'],
            feat['feat_x'],
            feat['feat_y'],
            feat['feat_w'],
            feat['feat_h'])
        if ret <> res_succs:
            return ret, data
        deva = feat['deva']
        if deva == -1:
            deva = conf.configure.template_default_deva
        mcnt = feat['mcnt']
        if mcnt == -1:
            mcnt = conf.configure.template_default_mcnt

        # return six matched point
        ret, d = self._template_itfc.match(pic_info._url, feat_url)
        if ret <> res_succs:
            return ret, data
        loc_info = {}
        max_cnt = 0
        max_loc = []
        for e in d:
            x = e[0]
            y = e[1]
            k = ''
            for kv, vl in loc_info.items():
                if abs(x - vl['kx']) <= deva and abs(y - vl['ky']) <= deva:
                    k = kv
                    break
            if k == '':
                k = str(x) + '.' + str(y)
            if loc_info.has_key(k):
                loc_info[k]['cnt'] = loc_info[k]['cnt'] + 1
            else:
                inf = {}
                inf['cnt'] = 1
                inf['kx'] = x
                inf['ky'] = y
                inf['loc'] = []
                loc_info[k] = inf
            l = []
            l.append(x)
            l.append(y)
            loc_info[k]['loc'].append(l)

            if max_cnt < loc_info[k]['cnt']:
                max_cnt = loc_info[k]['cnt']
                max_loc = loc_info[k]['loc']

        if max_cnt >= mcnt:
            for l in max_loc:
                info = {}
                info['x'] = l[0]
                info['y'] = l[1]
                data.append(info)
        return ret, data



    def run(self):
        ret = res_fail
        result = []
        ret, feats = self._template_itfc.feature_get(self._cls, self._pic_info._width, self._pic_info._height)
        if ret <> res_succs:
            logging.getLogger('error').error('feature_get fail with width[%d] height[%d]',
                                             self._pic_info._width, self._pic_info._height)
            return ret, result
        for feat in feats:
            r, d = self.match_feature(self._pic_info, feat)
            if r <> res_succs:
                continue
            if len(d) == 0:
                continue
            e = {}
            e['feat'] = feat
            e['result'] = d
            result.append(e)
        ret = res_succs
        return ret, result