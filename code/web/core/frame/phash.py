from ..intfc import img
from ..intfc import phash
from .. import conf
import logging
from ..defn.define import *

class pash_check_task:
    def __init__(self, phash_itfc, img_itfc, category, pic_info):
        self._phash_itfc = phash_itfc
        self._img_itfc = img_itfc
        self._category = category
        self._pic_info = pic_info

    def match_feat(self, pic_url, x, y, w, h, feat_url):
        ret = res_fail
        dist = -1
        while (True):
            ret, pic_url = self._img_itfc.gen_url(pic_url, x, y, w, h)
            if ret <> res_succs:
                logging.getLogger('error').error('gen_url fail with url[%s] x[%d] y[%d]',
                                                 pic_url, x, y)
                break
            ret, dist = self._phash_itfc.match(pic_url, feat_url)
            if ret <> res_succs:
                logging.getLogger('error').error('match fail with src_url[%s] dst_url[%s]',
                                                 pic_url, feat_url)
                break
            ret = res_succs
            break
        return ret, dist


    def match_feature(self, pic_info, feat):
        scale = float(pic_info._width) / float(feat['pic_wid'])
        feat_x = int(feat['feat_x'] * scale)
        feat_y = int(feat['feat_y'] * scale)
        feat_w = int(feat['feat_w'] * scale)
        feat_h = int(feat['feat_h'] * scale)
        feat_x_range = int(feat['feat_x_range'] * scale)
        feat_y_range = int(feat['feat_y_range'] * scale)

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
        dist = feat['dist']
        if dist == -1.0:
            dist = conf.configure.phash_default_dist
        for x in range(feat_x - feat_x_range, feat_x + feat_x_range + 1):
            for y in range(feat_y - feat_x_range, feat_y + feat_y_range + 1):
                r, d = self.match_feat(pic_info._url, x, y, feat_w, feat_h, feat_url)
                if r <> res_succs:
                    continue
                if ret <> res_succs:
                    ret = res_succs
                if d > dist:
                    continue
                info = {}
                info['x'] = x
                info['y'] = y
                info['dist'] = d
                data.append(info)
        return ret, data

    def run(self):
        ret = res_fail
        result = []
        ret, feats = self._phash_itfc.feature_get(self._category, self._pic_info._width, self._pic_info._height)
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