import phash
import template
from .. import intfc
from ..conf import configure
from ..defn.define import *

class checker:
    def __init__(self, cls, pic_url):
        self._cls = cls
        self._pic_url = pic_url
        self._phash_interface = intfc.phash.pash_interface(
            configure.engine_srv_url,
            configure.feature_srv_url)
        self._template_interface = intfc.template.template_interface(
            configure.engine_srv_url,
            configure.feature_srv_url)
        self._img_interface = intfc.img.img_interface()

    def phash_check(self, info):
        phash_task = phash.pash_check_task(self._phash_interface, self._img_interface, self._cls, info)
        ret, result = phash_task.run()
        return ret, result


    def template_check(self, info):
        template_task = template.template_check_task(self._template_interface, self._img_interface, self._cls, info)
        ret, result = template_task.run()
        return ret, result


    def run(self):
        ret = res_fail
        result = {}
        while (True):
            ret, info = self._img_interface.fetch(self._pic_url)
            if ret <> res_succs:
                break
            r_phash, s_phash = self.phash_check(info)
            if r_phash == res_succs:
                result['phash'] = s_phash
            else:
                result['phash'] = {}
            r_template, s_template = self.template_check(info)
            if r_template == res_succs:
                result['template'] = s_template
            else:
                result['template'] = {}

            ret = res_succs
            break
        return ret, result
