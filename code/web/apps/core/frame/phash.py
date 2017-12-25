from ..intfc import img
from ..intfc import phash
from .. import conf
import logging
from ..defn.define import *

class pash_check_task:
    def __init__(self, phash_itfc, img_itfc, cls, pic_info):
        self._phash_itfc = phash_itfc
        self._img_itfc = img_itfc
        self._cls = cls
        self._pic_info = pic_info

    def match_feat(self, url_s, feat_url):
        ret = res_fail
        result = []
        url_d = []
        url_d.append(feat_url)

        ret, data = self._phash_itfc.match_multiple(url_s, url_d)
        if ret <> res_succs:
            logging.getLogger('all').error('match fail with ret[%d]', ret)
            return ret, result
        ret = res_succs
        result = data
        return ret, result


    def match_feature(self, pic_info, feat):
        ret = res_fail
        data = []

        scale = float(pic_info._width + pic_info._height) / float(feat['pic_wid'] + feat['pic_high'])
        if abs(scale - 1) < conf.configure.phash_default_scale_deva:
            scale = 1

        # TODO:unsupport zoom yet
        if scale <> 1.0:
            return ret, data

        feat_x = int(feat['feat_x'] * scale)
        feat_y = int(feat['feat_y'] * scale)
        feat_w = int(feat['feat_w'] * scale)
        feat_h = int(feat['feat_h'] * scale)
        feat_x_range = int(feat['feat_x_range'] * scale)
        feat_y_range = int(feat['feat_y_range'] * scale)

        ret, feat_url = self._img_itfc.gen_url(
            feat['pic_url'],
            feat['feat_x'],
            feat['feat_y'],
            feat['feat_w'],
            feat['feat_h'])
        if ret <> res_succs:
            return ret, data
        dist = feat['dist']
        if dist == -1.0:
            dist = conf.configure.phash_default_dist

        url_s = []
        url_data_map = {}
        for x in range(0 if feat_x < feat_x_range else feat_x - feat_x_range, feat_x + feat_x_range + 1):
            for y in range(0 if feat_y < feat_y_range else feat_y - feat_y_range, feat_y + feat_y_range + 1):
                ret, u = self._img_itfc.gen_url(pic_info._url, x, y, feat_w, feat_h)
                if ret <> res_succs:
                    logging.getLogger('all').error('gen_url fail with url[%s] x[%d] y[%d]',
                                                   pic_info._url, x, y)
                    continue
                url_s.append(u)
                d = {}
                d['x'] = x
                d['y'] = y
                url_data_map[u] = d

        r, rd = self.match_feat(url_s, feat_url)
        if r <> res_succs:
            return ret, data
        for k,v in rd.items():
            u_s = k
            for kx, vx in v.items():
                u_d = kx
                d = vx
                if d > dist:
                    continue
                info = {}
                info['x'] = url_data_map[u_s]['x']
                info['y'] = url_data_map[u_s]['y']
                info['dist'] = d
                data.append(info)
        return ret, data

    def run(self):
        ret = res_fail
        result = []
        ret, feats = self._phash_itfc.feature_get(self._cls, self._pic_info._width, self._pic_info._height)
        if ret <> res_succs:
            logging.getLogger('all').error('feature_get fail with width[%d] height[%d]',
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